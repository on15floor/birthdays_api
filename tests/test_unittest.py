from tornado.testing import AsyncHTTPTestCase

import web
from config import Constants
from urllib.parse import urlencode
from models.exceptions import *

login_data_user_valid = {
    'email': 's.ivanov@lab15.ru',
    'password': 'UserPassword123',
}
login_data_user_invalid = {
    'email': 's.ivanov@lab15.ru',
    'password': '000000000000000',
}
login_data_admin_valid = {
    'email': 'a.anisimov@lab15.ru',
    'password': 'AdminPassword123',
}


class BasicTestsClass(AsyncHTTPTestCase):
    """ Базовый класс для тестовых кейсов
    """
    def get_app(self):
        return web.make_app()


class TestsCommonMethods(BasicTestsClass):
    """ Кейс тестов для общих методов API
    """
    def test_v1_ping(self):
        response = self.fetch('/v1/ping', method="GET")
        self.assertEqual(response.code, 200)
        self.assertIn('Pong', str(response.body))

    def test_v1_version(self):
        response = self.fetch('/v1/version', method="GET")
        self.assertEqual(response.code, 200)
        self.assertIn(Constants.VERSION, str(response.body))


class TestsUserMethods(BasicTestsClass):
    """ Кейс тестов для методов пользователя
    """
    def test_v1_user_auth_valid(self):

        response = self.fetch('/v1/user/auth', method="POST", body=urlencode(login_data_user_valid))
        self.assertEqual(response.code, 200)
        self.assertIn('success', str(response.body))

    def test_v1_user_auth_invalid(self):
        response = self.fetch('/v1/user/auth', method="POST", body=urlencode(login_data_user_invalid))
        self.assertEqual(response.code, 403)
        self.assertRaises(AUTH_FAILED_WRONG_PASS)
