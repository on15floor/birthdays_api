from models.exceptions import ACCESS_DENIED, BIRTHDAY_NOT_FOUND
from utils.database import SQLite3Instance


class Birthdays:
    def __init__(self, user_id):
        self.user_id = user_id
        self.db = SQLite3Instance()

    def get_birthdays(self) -> list:
        """ Метод получает все записи ДР
        :return: list(dict)
        """
        where_condition = f'WHERE user_id={self.user_id}'
        query = self.db.select('birthdays', [], where=where_condition)
        return query

    def add_birthday(self, in_data):
        """ Метод добавления ДР
        :param in_data: словарь входных данных (name, gender, birthday, comment)
        :return: None
        """
        in_data['user_id'] = self.user_id
        self.db.insert('birthdays', in_data)

    def del_birthday(self, birthday_id):
        """ Метод удаления ДР
        :param birthday_id: идентификатор др
        :return: None
        """
        # Проверка существования ДР с данным id
        where_condition = f'WHERE id={birthday_id}'
        query = self.db.select('birthdays', ['user_id'], where_condition)
        if not query:
            raise BIRTHDAY_NOT_FOUND
        # Проверяем принадлежность ДР с данных id пользователю
        if query[0]['user_id'] != self.user_id:
            raise ACCESS_DENIED
        # Удаляем
        self.db.delete('birthdays', where_condition)
