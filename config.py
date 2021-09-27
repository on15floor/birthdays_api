import os
from dotenv import load_dotenv

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
