import logging

from tornado.ioloop import IOLoop
from tornado.web import Application

from config import Constants
from urls import APP_URLS


def make_app():
    return Application(APP_URLS, debug=Constants.DEBUG)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info(f'[i] Debug mode: {Constants.DEBUG}')
    logging.info(f'[i] Running at port: {Constants.PORT}')
    app = make_app()
    app.listen(Constants.PORT)
    IOLoop.current().start()
