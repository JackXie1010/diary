# coding: utf8
import os
import peewee_async

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf = dict(
    test_env=False,
    static_path=basedir + "/static",
    static_url_prefix="/static/",
    template_path="templates",
    secret_key="Cb4EUsL39NHFqKo5",
    jwt_expire=15 * 24 * 3600,
    MEDIA_ROOT=os.path.join(basedir, "media"),
    SITE_URL="http://127.0.0.1:8888",
    redis={
        "host": "127.0.0.1"
    }
)

conf_test = dict(
    test_env=True,
    static_path=basedir + "/static",
    static_url_prefix="/static/",
    template_path="templates",
    secret_key="ZGGA#Mp4yL4w5CDu",
    jwt_expire=15 * 24 * 3600,
    MEDIA_ROOT=os.path.join(basedir, "media"),
    SITE_URL="http://127.0.0.1:8888",
    redis={
        "host": "127.0.0.1"
    }
)

database = peewee_async.PooledPostgresqlDatabase(
    'xzj', host="94.191.93.112", port=5432, user="postgres", password="xxx", max_connections=50
)
