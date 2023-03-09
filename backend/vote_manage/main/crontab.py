from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from django.db.models import Q, F
from main.tools import getTodayBeginTimeStamp, getNowTimeStamp, isSameDay, getTimeStr
from main.views.statics.StaticsOp import StaticsOp
import datetime

def updateStaticHistory():
    try:
        nowTime = getNowTimeStamp()
        nowTimeStr = getTimeStr(nowTime)
        yesterdayBeginTime = getTodayBeginTimeStamp(nowTime - 10)

        staticsOp = StaticsOp()
        yesterdayIncome =  staticsOp.queryYesterdayIncome(nowTime)
        models.StaticsHistory.objects.create(
            day_income = yesterdayIncome,
            day_time = yesterdayBeginTime,
            create_time = nowTime
        ).save()
        print('{} 更新统计历史成功\n'.format(nowTimeStr))
    except Exception as e:  
        print('{} 更新统计历史失败 {}\n'.format(nowTimeStr, str(e)))

def clearAllDomainVisitCount():
    try:
        nowTime = getNowTimeStamp()
        nowTimeStr = getTimeStr(nowTime)
        domainObj = models.Domain.objects.all()
        if domainObj:
            domainObj.update(visit_count=0)
        print('{} 重置域名访问量成功\n'.format(nowTimeStr))
    except Exception as e:  
        print('{} 重置域名访问量失败 {}\n'.format(nowTimeStr, str(e)))

def clearKeys():
    try:
        nowTime = getNowTimeStamp()
        nowTimeStr = getTimeStr(nowTime)
        models.Keys.objects.filter(Q(expire_time__lt=nowTime) | ~Q(has_used=0)).delete()
        print('{} 清除keys成功\n'.format(nowTimeStr))
    except Exception as e:
        print('{} 清除keys失败 {}\n'.format(nowTimeStr, str(e)))

