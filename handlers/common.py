from tornado.web import RequestHandler
from utils.mixins import WriteJSONMixin
from config import Constants
from utils.database import Map
from models.exceptions import AUTH_TOKEN_EMPTY, AUTH_TOKEN_INVALID
from models.user import User


class CommonHandler(RequestHandler, WriteJSONMixin):
    """ Общий класс методов
    """
    token = None

    def initialize(self) -> None:
        self.in_data = Map({})


class UserAuthHandler(CommonHandler):
    """ Класс методов, требующий авторизации пользователя
    """
    def check_user_auth(self):
        token = self.request.headers.get('auth-token')
        token_param = self.request.arguments.pop('token', '')
        if token_param:
            token = token_param[0].decode('utf-8')
        if not token:
            raise AUTH_TOKEN_EMPTY
        self.user = User.by_token(token)
        if not self.user:
            raise AUTH_TOKEN_INVALID

    def prepare(self):
        self.check_user_auth()


class Ping(CommonHandler):
    """ Метод проверки доступности сервера

    Входные параметры: Отсутствуют

    Пример успешного ответа:

    .. sourcecode: json

        {
            "message": "Pong"
        }

    """
    def get(self):
        self.jwrite({'message': 'Pong'})


class Version(CommonHandler):
    """ Метод получает версию API

    Входные параметры: Отсутствуют

    Пример успешного ответа:

    .. sourcecode: json

        {
            "message": "Version: 1.00"
        }

    """
    def get(self):
        self.jwrite({'message': f'Version: {Constants.VERSION}'})
