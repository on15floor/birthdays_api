from uuid import uuid4

from models.exceptions import AUTH_FAILED_WRONG_PASS, NOT_ENOUGH_DATA_TO_QUERY
from utils.crypt import check_pw
from utils.database import SQLite3Instance
from datetime import datetime, timedelta


class User:
    def __init__(self, user_id: int = None):
        self.db = SQLite3Instance()
        self.user_id = user_id
        self.email = None
        self.password = None
        self.role_id = None
        if self.user_id:
            data = self.update_data_from_sql(user_id=self.user_id)
            self.update(**data)

    def update(self, **kwargs):
        """ Обновляет данные класса
        :param kwargs: user_id, email, password, role_id
        :return: None
        """
        if kwargs:
            self.__dict__.update(**kwargs)

    def update_data_from_sql(self, user_id: int = None, email: str = None) -> dict:
        """ Выбирает данные из БД
        :param user_id: id пользователя
        :param email: email пользователя
        :return: dict = raw from users.sql
        """
        if user_id:
            where_condition = f'WHERE id="{user_id}"'
        elif email:
            where_condition = f'WHERE email="{email}"'
        else:
            raise NOT_ENOUGH_DATA_TO_QUERY
        db_raw = self.db.select('users', [], where=where_condition)
        return db_raw[0]

    def login_by_email(self, email: str, password: str):
        """ Метод логина пользователя
        :param email: email пользователя
        :param password: пароль пользователя
        :return:
        """
        data = self.update_data_from_sql(email=email)
        if not check_pw(password, data['password']):
            raise AUTH_FAILED_WRONG_PASS
        self.update(**data)

    def generate_auth_token(self):
        """ Метод генерирует новый токен авторизации для пользователя
        :return: auth_token: str (uuid4)
        """
        if not self.user_id:
            raise NOT_ENOUGH_DATA_TO_QUERY
        else:
            token = str(uuid4())
            sql = {
                'user_id': self.user_id,
                'token': token,
                'token_expired': datetime.now() + timedelta(days=1)
            }
            self.db.insert('users_tokens', sql)
        return token
