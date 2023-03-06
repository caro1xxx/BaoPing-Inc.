from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from django.db.models import *
from main.tools import getTodayBeginTimeStamp, getNowTimeStamp, isSameDay
from main.views.statics.StaticsOp import StaticsOp


class Crontab:
    def updateStaticHistory(self):
        try:
            nowTime = getNowTimeStamp()
            yesterdayBeginTime = getTodayBeginTimeStamp(nowTime - 10)
            staticsOp = StaticsOp()
            yesterdayIncome =  staticsOp.queryYesterdayIncome(nowTime)
            models.StaticsHistory.objects.create(
                day_income = yesterdayIncome,
                day_time = yesterdayBeginTime,
                create_time = nowTime
            ).save()
            print('更新统计历史成功')
        except Exception as e:  
            print('更新统计历史失败')

    def clearAllDomainVisitCount(self):
        domainObj = models.Domain.objects.all()
        if domainObj:
            domainObj.update(visit_count=0)

    def test(self):
        print('test method test')
        return 'test method test retun'

