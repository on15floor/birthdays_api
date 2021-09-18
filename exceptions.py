from tmp.tornadotools.exceptions import BaseAPIException

DB_CONNECTION_FAILED = BaseAPIException(
    error_type='db_connection_failed',
    error_descr='Database connection failed',
    error_descr_rus='Ошибка при подключении к базе данных',
)
