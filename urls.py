from handlers import common, user, admin

APP_URLS = [
    # Служебные методы
    # Метод проверки доступности сервера
    ('/v1/ping', common.Ping),
    # Метод получает версию API
    ('/v1/version', common.Version),

    # Методы пользователя
    # Метод авторизации
    ('/v1/user/auth', user.Auth),
    # Метод регистрации
    ('/v1/user/registration', user.Registration),

    # Методы администратора
    # Метод удаления пользователя
    ('/v1/admin/delete_user', admin.DeleteUser),
]
