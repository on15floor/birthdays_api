from datetime import datetime
from functools import wraps
from logging import info, exception

import jsonschema

from utils.objects import Map

RESERVED_PARAMETER_NAMES = {
    'token',
    'default_params',
    'input_json_d',
    'input_json_nt',
    'post_schema',
    'path_schema',
    'put_schema',
    'request'
}


def in_data_required(schema=None, log_errors=True):
    """ Декоратор проверяет валидность входных параметров по схеме.
    Если данные валидны, они помещаются в self.in_data (type: Map).
    Данные передаются в виде набора параметров формы: 'Content-Type': 'application/x-www-form-urlencoded' """

    def params_wrapper(func):
        @wraps(func)
        def func_wrapper(instance, *args, **kwargs):
            request_parameters = set(schema['properties'].keys())
            reserved_names_found = RESERVED_PARAMETER_NAMES.intersection(request_parameters)

            if reserved_names_found:
                instance.set_status(500, log_msg='reserved_parameters_name')
                info('reserved parameters name(s) found %s - please use '
                     'different name(s)' % ','.join(reserved_names_found))
                instance.finish()
                return

            if not schema:
                instance.set_status(500, log_msg='no_schema')
                info('no_schema')
                instance.finish()
                return

            if not hasattr(instance, 'in_data'):
                setattr(instance, 'in_data', Map({}))

            for parameter_name in request_parameters:
                arg = instance.get_argument(parameter_name, getattr(instance, parameter_name, None))
                if arg is not None:
                    instance.in_data[parameter_name] = arg
                setattr(instance, parameter_name, arg)

            try:
                jsonschema.validate(instance.in_data, schema, format_checker=jsonschema.FormatChecker())
            except jsonschema.ValidationError as e:
                instance.set_status(400)
                instance.jwrite({'status': 'error',
                                 'type': 'json_schema_validation_failed',
                                 'message': 'JSON did not match schema for this request'
                                            'Context: "{cont}". Reason: "{mes}"'.format(
                                             mes=e.message, cont='; '.join([val.message for val in e.context])),
                                 'extra': {'schema': e.schema}
                                 })
                if log_errors:
                    exception(e.message)
                instance.finish()
                return
            return func(instance, *args, **kwargs)

        return func_wrapper

    return params_wrapper


def print_func_duration(func):
    """ Выводит время выполнения функции """

    def inner(*args, **kwargs):
        start_time = datetime.now()
        print(f'[t]> {func.__name__}() start: {start_time.strftime("%Y-%m-%d, %H:%M:%S")}')
        res = func(*args, **kwargs)
        stop_time = datetime.now()
        print(f'[t]> {func.__name__}() stop: {stop_time.strftime("%Y-%m-%d, %H:%M:%S")}')
        exec_time = stop_time - start_time
        print(f'[t]> {func.__name__}() execution time: {exec_time.seconds * 1000 + exec_time.microseconds / 1000}ms')
        return res

    return inner
