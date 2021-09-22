from handlers.common import UserAuthHandler, CommonHandler
from utils.decorators import in_data_required
from models.user import User


class Auth(CommonHandler):
    """ Метод авторизации

    :reqheader Content-Type: 'application/x-www-form-urlencoded'

    Входные параметры:

    :fparam email: почта
    :fparam password: пароль

    Пример успешного ответа:

    .. sourcecode: json

        {
            "status": "success",
            "auth-toke": "6fd56840-fe22-49a7-a49b-a62050018adb"
        }

    - status - статус
    - auth-token - токен авторизации

    """

    AUTH_SCHEMA = {
        'type': 'object',
        'properties': {
            'email': {'type': 'string', 'pattern': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'},
            'password': {'type': 'string', 'minLength': 5, 'maxLength': 100},
        },
        'required': [
            'email',
            'password',
        ],
        'additionalProperties': False
    }

    @in_data_required(AUTH_SCHEMA)
    def post(self):
        user = User()
        user.login_by_email(self.in_data.email, self.in_data.password)

        self.jwrite({
            'status': 'success',
            'auth-token': user.generate_auth_token()
        })


class Registration(CommonHandler):
    """ Метод регистрации

    :reqheader Content-Type: 'application/x-www-form-urlencoded'

    Входные параметры:

    :fparam email: почта
    :fparam password: пароль
    :fparam first_name: имя
    :fparam last_name: фамилия

    Пример успешного ответа:

    .. sourcecode: json

        {
            "status": "success"
        }

    - status - статус

    Пример не успешного ответа:

    .. sourcecode: json

        {
            "status": "success"
            "status_code": 403,
            "error_type": "user_already_registered",
            "error_descr": "User already registered",
            "error_descr_rus": "Пользователь уже зарегистрирован",
        }

    """

    REGISTRATION_SCHEMA = {
        'type': 'object',
        'properties': {
            'email': {'type': 'string', 'pattern': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'},
            'password': {'type': 'string', 'minLength': 5, 'maxLength': 100},
            'last_name': {'type': 'string', 'minLength': 1, 'maxLength': 100},
            'first_name': {'type': 'string', 'minLength': 1, 'maxLength': 100},
        },
        'required': [
            'email',
            'password',
            'last_name',
            'first_name'
        ],
        'additionalProperties': False
    }

    @in_data_required(REGISTRATION_SCHEMA)
    def post(self):
        user = User()
        user.registration(self.in_data)
        self.jwrite({
            'status': 'success'
        })
