from uuid import uuid4

from models.exceptions import AUTH_FAILED_WRONG_PASS, NOT_ENOUGH_DATA_TO_QUERY, AUTH_TOKEN_EXPIRED, \
    USER_ALREADY_REGISTERED, ACCESS_DENIED, USER_NOT_FOUND
from utils.crypt import check_pw, hash_pw
from utils.database import SQLite3Instance
from datetime import datetime, timedelta


class User:
    def __init__(self, user_id: int = None):
        self.db = SQLite3Instance()
        self.user_id = user_id
        self.last_name = None
        self.first_name = None
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
            where_condition = f'WHERE user_id="{user_id}"'
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

    @classmethod
    def by_token(cls, token: str) -> 'User':
        """ Метод возвращает модель пользователя по токену
        :param token: токен авторизации
        :return: User (model)
        """
        # Ищем токен в базе данных
        db = SQLite3Instance()
        where_condition = f'WHERE token="{token}"'
        user_db = db.select('users_tokens', ['user_id', 'token_expired'], where=where_condition)
        # Проверяем его на действительность
        token_expired = user_db[0]['token_expired']
        time_expired = datetime.strptime(token_expired[:19], '%Y-%m-%d %H:%M:%S')
        if datetime.now() > time_expired:
            raise AUTH_TOKEN_EXPIRED
        # Возвращаем модель
        user_id = user_db[0]['user_id']
        return cls(user_id=user_id)

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

    @staticmethod
    def registration(data: dict) -> bool:
        """ Метод регистрации нового пользователя
        :param data: словарь данных для регистрации
        :return: auth_token: str (uuid4)
        """
        # Проверяем есть данный пользователь в БД
        if user_exist(data['email']):
            raise USER_ALREADY_REGISTERED
        # Формируем запись и вставляем в БД
        pwd = data.pop('password')
        data['password'] = hash_pw(pwd)
        data['role_id'] = 2
        db = SQLite3Instance()
        db.insert('users', data)
        return True

    # Методы Администратора
    def is_admin(self) -> bool:
        """ Метод проверяет статус администратора у пользователя
        :return: bool
        """
        if self.role_id == 1:
            return True

    def delete_user(self, email):
        """ Метод удаляет пользователя
        :param email: почта пользователя для удаления
        :return: bool
        """
        # Проверяем права администратора
        if not self.is_admin():
            raise ACCESS_DENIED
        # Проверяем есть данный пользователь в БД
        if not user_exist(email):
            raise USER_NOT_FOUND
        # Удаляем пользователя
        where_condition = f'WHERE email="{email}"'
        self.db.delete('users', where_condition)

    def get_statistic(self) -> list:
        """ Метод получения статистики по ДР
        :return: List[Dict] статистика
        """
        # Проверяем права администратора
        if not self.is_admin():
            raise ACCESS_DENIED
        sql_statement = '''
                SELECT users.user_id, users.email, count(users.email) as birthdays_count,
                --birthdays.id as birthdays_id,
                users_roles.role_name
                FROM users 
                LEFT JOIN birthdays ON users.user_id = birthdays.user_id
                LEFT JOIN users_roles ON users.role_id = users_roles.id
                WHERE birthdays.id NOT NULL
                GROUP BY users.email
        '''
        return self.db.pure_select(sql_statement=sql_statement)



def user_exist(email) -> bool:
    """ Метод проверяет существование учетной записи в базе данных
    :param email: почта пользователя
    :return: bool
    """
    db = SQLite3Instance()
    where_condition = f'WHERE email="{email}"'
    user_db = db.select('users', ['user_id'], where=where_condition)
    if user_db:
        return True
