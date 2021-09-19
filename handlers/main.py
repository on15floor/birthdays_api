from tornado.web import RequestHandler
from utils.mixins import WriteJSONMixin
from config import Constants


class CommonHandler(RequestHandler, WriteJSONMixin):
    pass


class Ping(CommonHandler):
    def get(self):
        self.jwrite({'message': 'Pong'})


class Version(CommonHandler):
    def get(self):
        self.jwrite({'message': f'Version: {Constants.VERSION}'})
