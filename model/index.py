# coding: utf8
from peewee import *
from model.base import BaseModel
from datetime import date


class Diary(BaseModel):
    sth = CharField(max_length=200)
    tags = CharField(max_length=100)
    remark = CharField(max_length=200)
    addTime = DateTimeField(default=date.today())

    class Meta:
        table_name = 'diary'
