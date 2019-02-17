# coding: utf8
from tornado import web
from handler import index

url_route = [
    (web.url('/', index.head)),
    (web.url('/addDiary', index.addDiary)),
    (web.url('/delDiary', index.delDiary)),
    (web.url('/updateDiary', index.updateDiary)),
    (web.url('/queryDiary', index.queryDiary)),
]