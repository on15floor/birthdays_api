import os

# База данных
DB_DIR = os.path.dirname(os.path.abspath(__name__))
DB_NAME = 'db_api.db'


class Constants:
    VERSION = '1.00'
    DEBUG = True
    PORT = 8888
