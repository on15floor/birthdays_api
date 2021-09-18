import os
from typing import Dict, List, Tuple
from config import DB_DIR

import sqlite3


conn = sqlite3.connect(os.path.join(DB_DIR, "db_api.db"))
cursor = conn.cursor()


def insert(table: str, column_values: Dict):
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
    cursor.executemany(f"INSERT INTO {table} "
                       f"({columns}) "
                       f"VALUES ({placeholders})",
                       values)
    conn.commit()


def fetchall(table: str, columns: List[str]) -> List[Tuple]:
    columns_joined = ", ".join(columns)
    cursor.execute(f"SELECT {columns_joined} FROM {table}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


def delete(table: str, row_id: int) -> None:
    row_id = int(row_id)
    cursor.execute(f"delete from {table} where id={row_id}")
    conn.commit()


def get_cursor():
    return cursor


def _init_db():
    """Инициализирует БД"""
    with open("createdb.sql", "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()


def check_db_exists():
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='expense'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


check_db_exists()


class NewSqlEngine(object):

    def __init__(self, db_name, lock=None):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._sql_config = {}
        self.RLock = lock

    def save(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def execute(self, *args, **kwargs):
        self.cursor.execute(*args, **kwargs)
        return self.cursor.fetchall()
