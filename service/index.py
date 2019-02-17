# coding: utf8
from service.base import BaseService, validate_arg, validate_token
from model.index import Diary
from playhouse.shortcuts import *


class IndexService(BaseService):
    async def addDiary(self, right_arg, arg, api):
        @validate_arg(right_arg, arg, api)
        def handler(): return 1
        result = handler()
        if 200 == result['code']:
            try:
                obj = await self.application.objects.create(Diary, **arg)
            except:
                obj = 0
            ret = self.finish_ok(msg='添加成功！') if obj else self.finish_err(msg='添加失败！', code=204)
        else:
            ret = result
        return ret

    async def delDiary(self, right_arg, arg):
        @validate_arg(right_arg, arg, '/delDiary')
        def handler(): return 1
        result = handler()
        if 200 == result['code']:
            try:
                sql = Diary.delete().where(Diary.id == arg['id'])
                num = await self.application.objects.execute(sql)
            except:
                num = 0
            ret = self.finish_ok(msg='删除成功') if num else self.finish_err(msg='删除失败', code=204)
        else:
            ret = result
        return ret

    async def updateDiary(self, right_arg, arg):
        @validate_arg(right_arg, arg, '/updateDiary')
        def handler(): return 1
        result = handler()
        if 200 == result['code']:
            try:  # success: num=1
                num = await self.application.objects.update(dict_to_model(Diary, arg, ignore_unknown=True))
            except:
                num = 0
            ret = self.finish_ok(msg='修改成功') if num else self.finish_err(msg='修改失败', code=204)
        else:
            ret = result
        return ret

    async def queryDiary(self, right_arg, arg):
        @validate_arg(right_arg, arg, '/queryDiary')
        def handler(): return 1
        result = handler()
        if 200 == result['code']:
            sql = Diary.select()
            data = await self.application.objects.execute(sql)
            lst = []
            for obj in data:
                lst.append(model_to_dict(obj))
            ret = self.finish_ok(data=lst)
        else:
            ret = result
        return ret
