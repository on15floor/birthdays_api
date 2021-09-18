from tornado.web import Application
from tornado.ioloop import IOLoop

from urls import APP_URLS


app = Application(APP_URLS)

if __name__ == '__main__':
    app.listen(8888)

    IOLoop.current().start()
