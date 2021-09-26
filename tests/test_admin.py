import json
from urllib.parse import urlencode

from tornado.httputil import HTTPHeaders

from tests import BasicTestsClass, login_data_admin_valid, registry_new_user, login_data_user_valid


class TestsAdminMethods(BasicTestsClass):
    """ Кейс тестов для методов администратора
    """
    def setUp(self) -> None:
        super().setUp()
        # Сформируем заголовок с токеном администратора
        response = self.fetch('/v1/user/auth', method="POST", body=urlencode(login_data_admin_valid))
        response_json = json.loads(response.body)
        self.headers = HTTPHeaders({'auth-token': response_json['auth-token']})

    def test_v1_admin_delete_user(self):
        response = self.fetch('/v1/admin/delete_user', method="POST",
                              body=urlencode({'email': registry_new_user['email']}), headers=self.headers)
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(response_json['status'], 'success')

    def test_v1_admin_delete_user_again(self):
        response = self.fetch('/v1/admin/delete_user', method="POST",
                              body=urlencode({'email': registry_new_user['email']}), headers=self.headers)
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 404)
        self.assertEqual(response_json['type'], 'user_not_found')

    def test_v1_admin_delete_not_admin(self):
        # Сформируем заголовок с токеном пользователя
        response = self.fetch('/v1/user/auth', method="POST", body=urlencode(login_data_user_valid))
        response_json = json.loads(response.body)
        self.headers = HTTPHeaders({'auth-token': response_json['auth-token']})

        response = self.fetch('/v1/admin/delete_user', method="POST",
                              body=urlencode({'email': registry_new_user['email']}), headers=self.headers)
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 403)
        self.assertEqual(response_json['type'], 'access_denied')
