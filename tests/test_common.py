import json

from config import Constants
from tests import BasicTestsClass


class TestsCommonMethods(BasicTestsClass):
    """ Кейс тестов для общих методов API
    """
    def test_v1_ping(self):
        response = self.fetch('/v1/ping', method="GET")
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(response_json['message'], 'Pong')

    def test_v1_version(self):
        response = self.fetch('/v1/version', method="GET")
        response_json = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(response_json['message'], f'Version: {Constants.VERSION}')
