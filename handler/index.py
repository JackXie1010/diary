# coding: utf8
from handler.base import BaseHandler
from service.index import IndexService


class head(BaseHandler):
    async def get(self):
        ret = self.finish_ok()
        self.write(self.to_json(ret))


class addDiary(BaseHandler):
    async def post(self):
        arg = self.to_dict(self.request.body)
        lst = await IndexService.addDiary(self, ['sth', 'tags', 'remark'], arg, '/addDiary')
        self.write(self.to_json(lst))


class delDiary(BaseHandler):
    async def post(self):
        arg = self.to_dict(self.request.body)
        ret = await IndexService.delDiary(self, ['id'], arg)
        self.write(self.to_json(ret))


class updateDiary(BaseHandler):
    async def post(self, *args, **kwargs):
        arg = self.to_dict(self.request.body)
        ret = await IndexService.updateDiary(self, ['id', 'sth', 'tags', 'remark'], arg)
        self.write(self.to_json(ret))


class queryDiary(BaseHandler):
    async def get(self, *args, **kwargs):
        ret = await IndexService.queryDiary(self, [], {'k': 'v'})
        self.write(self.to_json(ret))

