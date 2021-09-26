from tornado.testing import AsyncHTTPTestCase

import web

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
registry_new_user = {
    'email': 'test@test.ru',
    'password': 'testPassword',
    'first_name': 'Тест',
    'last_name': 'Тестов',
}
add_new_birthday = {
    'name': 'Тест Test',
    'gender': 'F',
    'birthday': '2000-10-20',
    'comment': 'test_comment',
}


class BasicTestsClass(AsyncHTTPTestCase):
    """ Базовый класс для тестовых кейсов
    """
    def get_app(self):
        return web.make_app()
