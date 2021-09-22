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
