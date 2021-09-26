import json
from urllib.parse import urlencode

from tests import BasicTestsClass, login_data_user_valid, login_data_user_invalid, registry_new_user


class TestsUserMethods(BasicTestsClass):
    """ Кейс тестов для методов пользователя
    """
    def test_v1_user_auth_valid(self):
        response = self.fetch('/v1/user/auth', method="POST", body=urlencode(login_data_user_valid))
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(response_json['status'], 'success')

    def test_v1_user_auth_invalid(self):
        response = self.fetch('/v1/user/auth', method="POST", body=urlencode(login_data_user_invalid))
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 403)
        self.assertEqual(response_json['type'], 'auth_failed_wrong_password')

    def test_v1_user_registration(self):
        response = self.fetch('/v1/user/registration', method="POST", body=urlencode(registry_new_user))
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(response_json['status'], 'success')

    def test_v1_user_registration_again(self):
        response = self.fetch('/v1/user/registration', method="POST", body=urlencode(registry_new_user))
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 400)
        self.assertEqual(response_json['type'], 'user_already_registered')
