from datetime import datetime as dt

from utils.objects import Map


def is_api_available(data: Map) -> bool:
    """ Функция проверяет доступность АПИ по временному интервалу
    :param data: Объект Map с настройками
    :return: bool
    """
    dt_from = data.get('unavailable_from_dt', '')
    if dt_from:
        dt_to = data.get('unavailable_to_dt', '3000-01-01 00:00:00')
        dt_from = dt.strptime(dt_from, '%Y-%m-%d %H:%M:%S')
        dt_to = dt.strptime(dt_to, '%Y-%m-%d %H:%M:%S')
        if dt_from < dt.now() < dt_to:
            return False
    return True
