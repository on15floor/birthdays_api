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
    error_type='auth_failed_wrong_password',
    error_descr='Auth Failed Wrong Password',
    error_descr_rus='Ошибка авторизации, неверный пароль',
)
NOT_ENOUGH_DATA_TO_QUERY = BaseAPIException(
    status_code=400,
    error_type='not_enough_data_to_query',
    error_descr='Not Enough Data To Query',
    error_descr_rus='Не достаточно данных',
)
AUTH_TOKEN_EMPTY = BaseAPIException(
    status_code=401,
    error_type='auth_token_empty',
    error_descr='Auth token empty',
    error_descr_rus='Токен авторизации отсутствует',
)
AUTH_TOKEN_INVALID = BaseAPIException(
    status_code=403,
    error_type='auth_token_invalid',
    error_descr='Auth token invalid',
    error_descr_rus='Токен авторизации не действительный',
)
AUTH_TOKEN_EXPIRED = BaseAPIException(
    status_code=403,
    error_type='auth_token_expired',
    error_descr='Auth token expired',
    error_descr_rus='Токе авторизации устарел',
)
