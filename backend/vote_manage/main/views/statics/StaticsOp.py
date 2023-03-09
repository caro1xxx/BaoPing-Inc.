from main import models
from django.db.models import *
from main.tools import getTodayBeginTimeStamp, getNowTimeStamp, isSameDay


class StaticsOp:
    def queryTimedeltaIncome(self, beginTime, endTime):
        sumIncome = models.PaymentRecord.objects.filter(
            create_time__gte = beginTime,
            create_time__lt = endTime,
            payment_status = 1
        ).aggregate(sum_income=Sum('price'))
        return sumIncome['sum_income'] if sumIncome['sum_income'] else 0
    
    def queryYesterdayIncome(self, nowTime):
        todayBeginTime = getTodayBeginTimeStamp(nowTime)
        yesterdayBeginTime = getTodayBeginTimeStamp(todayBeginTime - 1)
        sumIncome = self.queryTimedeltaIncome(yesterdayBeginTime, todayBeginTime)
        return sumIncome
    
    def queryTodayIncome(self, nowTime):
        todayBeginTime = getTodayBeginTimeStamp(nowTime)
        sumIncome = self.queryTimedeltaIncome(todayBeginTime, nowTime)
        return sumIncome
    
    def initStatics(self):
        nowTime = getNowTimeStamp()
        staticsOp = StaticsOp()
        todayIncome = staticsOp.queryTodayIncome(nowTime)
        yesterdayIncome = staticsOp.queryYesterdayIncome(nowTime)
        updateTime = nowTime
        staticsObj =  models.Statics.objects.create(
            today_income = todayIncome,
            yesterday_income = yesterdayIncome,
            update_time = updateTime,
        )
        staticsObj.save()
        return staticsObj

    def updateStatics(self):
        nowTime = getNowTimeStamp()
        staticsObj = models.Statics.objects.all().first()
        updateTime = staticsObj.update_time
        if isSameDay(updateTime, nowTime):
            addIncome = self.queryTimedeltaIncome(updateTime, nowTime)
            staticsObj.today_income += addIncome
        else:
            staticsObj.today_income = self.queryTodayIncome(nowTime)
            staticsObj.yesterday_income = self.queryYesterdayIncome(nowTime)
        staticsObj.update_time = nowTime    
        staticsObj.save()
        return staticsObj