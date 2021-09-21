from handlers import common, user

APP_URLS = [
    # Служебные методы
    # Метод проверки доступности сервера
    ('/v1/ping', common.Ping),
    # Метод получает версию API
    ('/v1/version', common.Version),

    # Методы пользователя
    # Метод авторизации
    ('/v1/user/auth', user.Auth),

]
