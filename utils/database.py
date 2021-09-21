import os
import sqlite3
from config import DB_DIR, DB_NAME


class Map(dict):
    """
    https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]


class SQLite3Instance:
    """ Класс (обертка) для работы с SQLite3 БД """
    def __init__(self):
        self.db_name = DB_NAME
        self.db_dir = DB_DIR
        self.con = sqlite3.connect(os.path.join(self.db_dir, self.db_name))
        self.cur = self.con.cursor()

    def select(self, table: str, columns: list[str], where: str = None) -> list[dict]:
        """ Метод выборки данных из БД
        :param table: таблица
        :param columns: какие колонки необходимо выбрать (необязательный параметр)
        :param where: дополнительные условия выборки (необязательный параметр)
        :return: Возвращает результат выборки из БД в формате: лист словарей
        """
        columns_joined = ', '.join(columns) if columns else '*'
        sql = f'SELECT {columns_joined} FROM {table} ' + where
        self.cur.execute(sql)
        return [dict(zip([desc[0] for desc in self.cur.description], row)) for row in self.cur.fetchall()]

    def insert(self, table: str, column_values: dict) -> None:
        """ Метод вставки данных в БД
        :param table: таблица
        :param column_values: словарь для вставки
        :return: None
        """
        columns = ', '.join(column_values.keys())
        values = [tuple(column_values.values())]
        placeholders = ', '.join('?' * len(column_values.keys()))
        sql = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        self.cur.executemany(sql, values)
        self.con.commit()

    def delete(self, table: str, where: str) -> None:
        """ Метод удаления данных из БД
        :param table: таблица
        :param where: дополнительные условия
        :return: None
        """
        sql = f'DELETE FROM {table} ' + where
        self.cur.execute(sql)
        self.con.commit()
