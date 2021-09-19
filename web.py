from tornado.web import Application
from tornado.ioloop import IOLoop
from config import Constants

from urls import APP_URLS


app = Application(APP_URLS, debug=Constants.DEBUG)

if __name__ == '__main__':
    print(f'[i] Debug mode: {Constants.DEBUG}')
    print(f'[i] Running at port: {Constants.PORT}')
    app.listen(Constants.PORT)

    IOLoop.current().start()
