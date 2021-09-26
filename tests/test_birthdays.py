import json
from urllib.parse import urlencode

from tornado.httputil import HTTPHeaders

from tests import BasicTestsClass, login_data_admin_valid, add_new_birthday


class TestsBirthdaysMethods(BasicTestsClass):
    """ Кейс тестов для методов работы с ДР
    """
    def setUp(self) -> None:
        super().setUp()
        # Сформируем заголовок с токеном пользователя
        response = self.fetch('/v1/user/auth', method="POST", body=urlencode(login_data_admin_valid))
        response_json = json.loads(response.body)
        self.headers = HTTPHeaders({'auth-token': response_json['auth-token']})

    def test_v1_birthdays_get(self):
        response = self.fetch('/v1/birthdays/get', method="GET", headers=self.headers)
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 200)

    def test_v1_birthdays_add(self):
        response = self.fetch('/v1/birthdays/add', method="POST",
                              body=urlencode(add_new_birthday), headers=self.headers)
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(response_json['status'], 'success')

    def test_v1_birthdays_del(self):
        # Сначала нужно найти id тестовой записи
        id_to_del = 0
        response = self.fetch('/v1/birthdays/get', method="GET", headers=self.headers)
        response_json = json.loads(response.body)
        for raw in response_json:
            if raw['comment'] == 'test_comment':
                id_to_del = raw['id']
                break

        response = self.fetch('/v1/birthdays/del', method="POST",
                              body=urlencode({'birthday_id': id_to_del}), headers=self.headers)
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(response_json['status'], 'success')

    def test_v1_birthdays_del_id_not_exist(self):
        id_to_del = 0
        response = self.fetch('/v1/birthdays/del', method="POST",
                              body=urlencode({'birthday_id': id_to_del}), headers=self.headers)
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 404)
        self.assertEqual(response_json['type'], 'birthday_not_found')

    def test_v1_birthdays_del_wrong_user(self):
        id_to_del = 5
        response = self.fetch('/v1/birthdays/del', method="POST",
                              body=urlencode({'birthday_id': id_to_del}), headers=self.headers)
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 403)
        self.assertEqual(response_json['type'], 'access_denied')
