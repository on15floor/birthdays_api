import os
import sqlite3
from typing import Dict, List


class SQLite3Instance:
    """ Класс (обертка) для работы с SQLite3 БД """
    def __init__(self, db_dir, db_name):
        self.db_name = db_name
        self.db_dir = db_dir
        self.con = sqlite3.connect(os.path.join(self.db_dir, self.db_name))
        self.cur = self.con.cursor()

    def select(self, table: str, columns: List[str]) -> List[Dict]:
        columns_joined = ', '.join(columns)
        self.cur.execute(f'SELECT {columns_joined} FROM {table}')
        rows = self.cur.fetchall()
        result = []
        for row in rows:
            dict_row = {}
            for index, column in enumerate(columns):
                dict_row[column] = row[index]
            result.append(dict_row)
        return result

    def insert(self, table: str, column_values: Dict) -> None:
        columns = ', '.join(column_values.keys())
        values = [tuple(column_values.values())]
        placeholders = ', '.join('?' * len(column_values.keys()))
        self.cur.executemany(f'INSERT INTO {table} '
                             f'({columns}) '
                             f'VALUES ({placeholders})', values)
        self.con.commit()

    def delete(self, table: str, param: str, val: str) -> None:
        self.cur.execute(f'DELETE FROM {table} WHERE {param}={val}')
        self.con.commit()
