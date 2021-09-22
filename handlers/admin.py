from handlers.common import UserAuthHandler
from utils.decorators import in_data_required


class DeleteUser(UserAuthHandler):
    """ Метод удаления пользователя

    :reqheader Content-Type: 'application/x-www-form-urlencoded'
    :reqheader auth-token: токен авторизации

    Входные параметры:

    :fparam email: почта пользователя

    Пример успешного ответа:

    .. sourcecode: json

        {
            "status": "success"
        }

    - status - статус

    Пример ответа для пользователей без статуса администратор:

    .. sourcecode: json

        {
            "status": "error",
            "status_code": 403,
            "error_type: "access_denied",
            "error_descr: "Access denied",
            "error_descr_rus: "Доступ запрещен",
        }

    Пример ответа, если пользовать не найден:

    .. sourcecode: json

        {
            "status": "error",
            "status_code": 404,
            "error_type: "user_not_found",
            "error_descr: "User not found",
            "error_descr_rus: "Пользователь не найден",
        }

    """

    DELETE_USER_SCHEMA = {
        'type': 'object',
        'properties': {
            'email': {'type': 'string', 'pattern': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'},
        },
        'required': [
            'email',
        ],
        'additionalProperties': False
    }

    @in_data_required(DELETE_USER_SCHEMA)
    def post(self):
        self.user.delete_user(self.in_data.email)

        self.jwrite({
            'status': 'success'
        })
