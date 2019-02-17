# coding: utf8
import jwt
import time
from conf import settings


def gen_token(id, username):
    payload = {
        "iss": "gusibi.com",
        "iat": int(time.time()),
        "exp": int(time.time()) + settings.conf['jwt_expire'],
        "aud": "www.gusibi.com",
        "uid": id,
        "username": username,
        "scopes": ['open']
    }
    token = jwt.encode(payload, settings.conf['secret_key'], algorithm='HS256')
    # return True, {'token': token, 'id': id}
    return token


def validate_token(token):
    try:
        #  如果在生成token的时候使用了aud参数，那么校验的时候也需要添加此参数
        payload = jwt.decode(token, settings.conf['secret_key'], audience='www.gusibi.com', algorithms=['HS256'])
        print(payload)
        if payload:
            return {'res': 1, 'msg': token}
        return {'res': 0, 'msg': token}
    except:
        return {'res': 0, 'msg': 'token超时或被篡改，请重新登陆'}


if __name__ == '__main__':
    token = gen_token(1, 'root')
    ret = validate_token(token)
    print(ret)