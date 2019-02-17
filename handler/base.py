# coding: utf8
from datetime import date
from tornado import web
import json


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.__str__()
        return json.JSONEncoder.default(self, obj)


class BaseHandler(web.RequestHandler):
    # 设置请求头
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, DELETE, PUT, PATCH, OPTIONS')
        self.set_header(
            'Access-Control-Allow-Headers',
            'Content-Type, token, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods'
        )

    def options(self, *args, **kwargs):
        pass

    def to_json(self, arg):
        try:
            res = json.dumps(arg, cls=DateEncoder)
        except:
            res = arg
        return res

    def to_dict(self, arg):
        try:
            res = json.loads(arg)
        except:
            res = arg
        return res

    def finish_ok(self, data=1, code=200, msg='请求成功'):
        obj = dict(code=code, data=data, msg=msg)
        return obj

    def finish_err(self, data=1, code=204, msg='请求失败'):
        obj = dict(code=code, data=data, msg=msg)
        return obj

