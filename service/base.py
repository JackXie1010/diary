# coding: utf8
from handler import base
from conf.jwt_token import validate_token


def validate_arg(right_arg, arg, api):
    def w(func):
        def inner():
            if type(right_arg) != list and type(arg) != dict:
                diff = 1
            else:
                diff = list(set(right_arg).difference(set(arg)))
            if diff:
                msg = '校验的参数格式错误' if 1 == diff else '缺少的参数有：%s' % diff
                ret = {'msg': msg, 'code': 604, 'data': ''}
            else:
                try:
                    data = func()
                    print('###### API ######## %s, params=%s' % (api, arg))
                    ret = {'msg': '', 'code': 200, 'data': data}
                except Exception:
                    ret = {'msg': '系统异常', 'code': 999, 'data': ''}
            return ret
        return inner
    return w

def validate_token(right_arg, arg, api):
    def w(func):
        def inner():
            if type(right_arg) != list and type(arg) != dict:
                diff = 1
            else:
                diff = list(set(right_arg).difference(set(arg)))
            if diff:
                msg = '校验的参数格式错误' if 1 == diff else '缺少的参数有：%s' % diff
                ret = {'msg': msg, 'code': 604, 'data': ''}
            else:
                try:
                    result = validate_token(arg['token'])  # result = {res:0/1, msg:payload}
                    if result['res']:
                        data = func()
                        print('###### API ######## %s, params=%s' % (api, arg))
                        ret = {'msg': '', 'code': 200, 'data': data}
                    else:
                        ret = {'msg': '用户信息有误，请重新登录', 'code': 204, 'data': 1}
                except Exception:
                    ret = {'msg': '系统异常', 'code': 999, 'data': ''}
            return ret
        return inner
    return w


class BaseService(base.BaseHandler):
    def __init__(self, *args, **kwargs):
        super(BaseService, self).__init__(*args, **kwargs)


