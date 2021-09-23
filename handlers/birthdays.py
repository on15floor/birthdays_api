from handlers.common import UserAuthHandler
from utils.decorators import in_data_required
from models.birthdays import Birthdays


class Get(UserAuthHandler):
    """ Метод получения списка всех ДР

    :reqheader Content-Type: 'application/x-www-form-urlencoded'
    :reqheader auth-token: токен авторизации

    Входные параметры отсутствуют:

    Пример успешного ответа:

    .. sourcecode: json

        [
            {
                "id": 3,
                "created_date": "2021-09-18 13:07:27",
                "user_id": 3,
                "name": "Федорова Алина Игоревна",
                "gender": "F",
                "birthday": "1993-12-13",
                "comment": "Школа"
            },
            {
                "id": 4,
                "created_date": "2021-09-18 13:07:27",
                "user_id": 3,
                "name": "Денисенко Василий Петрович",
                "gender": "M",
                "birthday": "1990-09-12",
                "comment": "Школа"
            }
        ]

    - id - идентификатор ДР
    - created_date - дата создания записи
    - user_id - идентификатор пользователя
    - name - имя именинника
    - gender - пол (M/F)
    - birthday - дата рождения
    - comment - комментарий

    """

    def get(self):
        birthdays = Birthdays(self.user.user_id)
        self.jwrite(birthdays.get_birthdays())


class Add(UserAuthHandler):
    """ Метод добавления нового ДР

    :reqheader Content-Type: 'application/x-www-form-urlencoded'
    :reqheader auth-token: токен авторизации

    Входные параметры:

    :fparam name: имя именинника
    :fparam gender: пол (M/F)
    :fparam birthday: дата рождения
    :fparam comment: комментарий

    Пример успешного ответа:

    .. sourcecode: json

        {
            "status": "success"
        }

    - status - статус

    """

    BIRTHDAYS_ADD = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'minLength': 1, 'maxLength': 300},
            'gender': {'type': 'string', 'minLength': 1, 'maxLength': 1},
            'birthday': {'type': 'string', 'pattern': r'^\d{4}-\d{2}-\d{2}$'},
            'comment': {'type': 'string', 'minLength': 1, 'maxLength': 300},
        },
        'required': [
            'name',
            'gender',
            'birthday',
            'comment',
        ],
        'additionalProperties': False
    }

    @in_data_required(BIRTHDAYS_ADD)
    def post(self):
        birthdays = Birthdays(self.user.user_id)
        birthdays.add_birthday(self.in_data)
        self.jwrite({
            'status': 'success'
        })


class Del(UserAuthHandler):
    """ Метод удаляет запись с ДР по его id

    :reqheader Content-Type: 'application/x-www-form-urlencoded'
    :reqheader auth-token: токен авторизации

    Входные параметры:

    :fparam birthday_id: id записи ДР, можно получить в методе /v1/birthdays/get

    Пример успешного ответа:

    .. sourcecode: json

        {
            "status": "success"
        }

    - status - статус

    Пример не успешного ответа:

    .. sourcecode: json

        {
            "status": "error"
            "status_code": 404,
            "error_type": "birthday_not_found",
            "error_descr": "Birthday not found",
            "error_descr_rus": "День рождения не найден",
        }

    """

    BIRTHDAYS_DEL = {
        'type': 'object',
        'properties': {
            'birthday_id': {'type': 'string'},
        },
        'required': [
            'birthday_id',
        ],
        'additionalProperties': False
    }

    @in_data_required(BIRTHDAYS_DEL)
    def post(self):
        birthdays = Birthdays(self.user.user_id)
        birthdays.del_birthday(self.in_data.birthday_id)
        self.jwrite({
            'status': 'success'
        })
