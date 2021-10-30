import os

from dotenv import load_dotenv

from utils.objects import Map

load_dotenv()

# База данных
DB_DIR = os.getenv('DB_DIR')
DB_NAME = os.getenv('DB_NAME')

# Директории
API_DIR = os.path.dirname(os.path.abspath(__name__))

NEED_LOG = {
    '/v1/user/auth',
    '/v1/user/registration',
    '/v1/admin/delete_user',
    '/v1/birthdays/get',
    '/v1/birthdays/add',
    '/v1/birthdays/del'
}


class Constants:
    VERSION = '1.00'
    DEBUG = os.getenv('DEBUG')
    PORT = 8888


api = Map({
    'unavailable_from_dt': '2021-10-28 05:00:00',
    'unavailable_to_dt': '2021-10-29 06:00:00',
})
