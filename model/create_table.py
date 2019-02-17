# coding: utf8
from model import index
from conf.settings import database


def init(database):
    database.create_tables([index.Diary])


if __name__ == "__main__":
    init(database)
    print('finish create table')
