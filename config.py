import os
from dotenv import load_dotenv

load_dotenv()

# База данных
DB_DIR = os.getenv('DB_DIR')
DB_NAME = os.getenv('DB_NAME')


class Constants:
    VERSION = '1.00'
    DEBUG = os.getenv('DEBUG')
    PORT = 8888
