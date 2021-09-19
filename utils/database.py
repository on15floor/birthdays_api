import os
import sqlite3
from typing import Dict, List
from config import DB_DIR, DB_NAME


class SQLite3Instance:
    """ Класс (обертка) для работы с SQLite3 БД """
    def __init__(self):
        self.db_name = DB_NAME
        self.db_dir = DB_DIR
        self.con = sqlite3.connect(os.path.join(self.db_dir, self.db_name))
        self.cur = self.con.cursor()

    def select(self, table: str, columns: List[str], where: str = None) -> List[Dict]:
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

    def insert(self, table: str, column_values: Dict) -> None:
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
