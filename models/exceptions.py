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


AUTH_FAILED_WRONG_PASS = BaseAPIException(
    status_code=403,
    status='error',
    error_type='auth_failed_wrong_password',
    error_descr='Auth Failed Wrong Password',
    error_descr_rus='Ошибка авторизации, неверный пароль',
)

NOT_ENOUGH_DATA_TO_QUERY = BaseAPIException(
    status_code=400,
    status='error',
    error_type='not_enough_data_to_query',
    error_descr='Not Enough Data To Query',
    error_descr_rus='Не достаточно данных',
)