from datetime import datetime


def print_func_duration(func):
    """Выводит время выполнения функции"""

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
