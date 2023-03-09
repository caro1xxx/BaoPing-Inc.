from celery import shared_task
from main import models
from main.tools import generateCode6
from django.core.mail import send_mail
from vote_manage import settings
from django.core.cache import cache
from main.views.vote_target.VoteTargetOp import VoteTargetOp
from openpyxl import load_workbook


@shared_task
def myTask():
    print('task test')
    models.Keys.objects.create(
        value = 'test',
        expire_time = '123412321',
        has_used = 1,
        user_agent_id = 'wxtest6'
    )

@shared_task
def sendEmail(email):
    try:
        code = generateCode6()
        content = code
        my_email = send_mail(
            '验证码', 
            '', 
            settings.DEFAULT_FROM_EMAIL, 
            [email], 
            html_message='<html lang="en"><body style="display: flex;justify-content: center;align-items: center;"><div style="width: 300px;background-color: #2479fb;padding: 20px;color: white;font-size: 20px;"><div style="text-align: center;">投票管理系统</div><div style="text-align: center;font-size: 15px;text-align: start;margin: 20px 0px;">您的验证码是:</div><div style="font-size: 30px;font-weight: bold;text-align: center;margin-top: 50px;">{}</div><div style="font-size: 10px;text-align: start;margin-top: 50px;">验证码有效期5分钟</div></div></body></html>'.format(code)
        )
        if my_email != 1:
            return False, '发送验证码失败'
        key = 'syl_' + email
        cache.set(key, code, 300)  
    except Exception as e:
        return False, '发送验证码失败', str(e)
    return True, '发送验证码成功'

@shared_task
def addVoteTargets(filename):
    path = str(settings.MEDIA_ROOT) + '/' + str(filename)
    wb = load_workbook(path)
    sheet = wb.worksheets[0]

    data, isFirst = [], True
    for row in sheet.rows:
        if isFirst:
            isFirst = False
            continue
        tmp = {}
        tmp['vote_id'] = row[0].value 
        tmp['name'] = row[1].value 
        tmp['detail'] = row[2].value 
        tmp['count'] = row[3].value 
        data.append(tmp)

    voteTargetOp = VoteTargetOp()
    for voteTarget in data:
        ok, msg = voteTargetOp.checkData(voteTarget['name'], voteTarget['detail'], voteTarget['vote_id'], voteTarget['count'])
        if ok:
            voteTargetOp.create(voteTarget)