from handlers import main

APP_URLS = [
    # Служебные методы
    ('/v1/ping', main.Ping),
    ('/v1/version', main.Version),
]
