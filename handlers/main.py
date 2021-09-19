from tornado.web import RequestHandler
from utils.mixins import WriteJSONMixin
from config import Constants


class CommonHandler(RequestHandler, WriteJSONMixin):
    pass


class Ping(CommonHandler):
    """ Метод проверки доступности сервера

    Входные параметры: Отсутствуют

    Пример успешного ответа:
    {
        'message': 'Pong'
    }

    """
    def get(self):
        self.jwrite({'message': 'Pong'})


class Version(CommonHandler):
    """ Метод получает версию API

    Входные параметры: Отсутствуют

    Пример успешного ответа:
    {
        'message': 'Version: 1.00'
    }

    """
    def get(self):
        self.jwrite({'message': f'Version: {Constants.VERSION}'})
