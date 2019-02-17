# coding: utf8
from tornado import web
from tornado import ioloop
from tornado.options import options, define
from peewee_async import Manager
from conf.settings import *
import route
import json
import logging

define("port", default=8888, help='default port', type=int)
define('debug', default=True, type=bool)
define('test', default=True, type=bool)
options.parse_command_line()


class Application(web.Application):
    def log_request(self, handler):
        if 'log_function' in self.settings:
            self.settings['log_function'](handler)
            return
        if handler.get_status() < 400:
            log_method = logging.info
        elif handler.get_status() < 500:
            log_method = logging.warning
        else:
            log_method = logging.error
        request_time = 1000.0 * handler.request.request_time()
        params = handler.request.body.decode("utf-8")
        if params.strip() != '':
            try:
                params = json.loads(params)
            except json.decoder.JSONDecodeError:
                params = {}
        else:
            params = {}
        log_method(
            "%d %s %s (%s) %.2fms params=%s",
            handler.get_status(),
            handler.request.method,
            handler.request.uri,
            handler.request.headers.get("X-Real-Ip", "127.0.0.1"),
            request_time,
            params
        )


def main():
    objects = Manager(database)
    app = Application(route.url_route, debug=options.debug, **conf)
    app.listen(options.port)
    database.set_allow_sync(False)
    app.objects = objects
    print("server is listening on http://127.0.0.1:%s" % options.port)
    io_loop = ioloop.IOLoop.instance()
    io_loop.start()


if __name__ == '__main__':
    main()
