from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from django.db.models import Q, F
from main.tools import getTodayBeginTimeStamp, getNowTimeStamp, isSameDay, getTimeStr
from main.views.statics.StaticsOp import StaticsOp
from main.views.voteuser.CommentOp import CommentOp
import datetime

def updateStaticHistory():
    try:
        nowTime = getNowTimeStamp()
        nowTimeStr = getTimeStr(nowTime)
        yesterdayBeginTime = getTodayBeginTimeStamp(nowTime - 10)

        if models.StaticsHistory.objects.filter(day_time=yesterdayBeginTime).first() is None:
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

def autoComment():
    try:
        autoCommentObj = models.AutoComment.objects.all()
        commentOp = CommentOp()
        nowTime = getNowTimeStamp()
        nowTimeStr = getTimeStr(nowTime)
        dayTime = nowTime % 86400

        for t in autoCommentObj:
            print('{} {} '.format(nowTimeStr, t.vote_target_id), end='')
            if nowTime < t.begin_time or nowTime > t.end_time:
                print('超出自动评论时间')
                t.delete()
                continue
            day_begin_time = t.day_begin_time + 8 * 3600 % 86400
            day_end_time = t.day_end_time + 8 * 3600 % 86400
            if dayTime < day_begin_time or dayTime > day_end_time:
                print('超出自动评论每日时间')
                continue
            if (nowTime - t.update_time) // 60 < t.space:
                print('超出自动评论时间间隔')
                continue
            if getTodayBeginTimeStamp(nowTime) != getTodayBeginTimeStamp(t.update_time):
                t.day_vote_count = 0
            if t.day_vote_count >= t.day_count_strict:
                print('超出自动评论数量限额')
                continue
            
            # vote
            commentOp.create({
                'vote_target_id': t.vote_target_id,
                'vote_user_open_id': 'wxxiaotest',
                'content': 'autocomment content',
                'status': 1
            })
            t.update_time = nowTime
            t.day_vote_count += 1
            t.save()
            # print('{} autocomment成功\n'.format(nowTimeStr))
        print('')
    except Exception as e:
        print('{} autocomment失败 {}\n'.format(nowTimeStr, str(e)))
    
def clearTempFiles():
    try:
        nowTime = getNowTimeStamp()
        nowTimeStr = getTimeStr(nowTime)
        models.TempFile.objects.all().delete()
        print('{} 清除临时文件成功\n'.format(nowTimeStr))
    except Exception as e:
        print('{} 清除临时文件失败 {}\n'.format(nowTimeStr, str(e)))