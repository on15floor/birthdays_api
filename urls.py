from handlers import main

APP_URLS = [
    # Служебные методы
    ('/v1/ping', main.ping()),
]
