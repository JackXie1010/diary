# coding: utf8
from conf.settings import database
from peewee import *


class BaseModel(Model):
    pass
    # add_time = DateTimeField(default=datetime.now, verbose_name="创建时间")
    # status = IntegerField(default=1, verbose_name="状态")

    class Meta:
        database = database
