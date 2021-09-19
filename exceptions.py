class BaseAPIException(Exception):
    def __init__(self, error_descr, error_type, error_descr_rus, status='error', status_code=400):
        assert isinstance(error_descr, str)
        assert isinstance(error_type, str)
        assert status in ['success', 'error']
        assert str(status_code).isdigit() and (100 <= int(status_code) < 600)
        assert len(error_type.split()) == 1

        self.error_descr = error_descr
        self.error_descr_rus = error_descr_rus
        self.error_type = error_type
        self.status = status
        self.status_code = status_code


DB_CONNECTION_FAILED = BaseAPIException(
    error_type='db_connection_failed',
    error_descr='Database connection failed',
    error_descr_rus='Ошибка при подключении к базе данных',
)
