from celery import shared_task
from main import models
from main.tools import generateCode6
from django.core.mail import send_mail
from vote_manage import settings
from django.core.cache import cache
from main.views.vote_target.VoteTargetOp import VoteTargetOp
from openpyxl import load_workbook
from main.views.task.TaskOp import TaskOp


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
def addVoteTargets(filename, taskId, voteId):
    message = 'success'
    try:
        path = str(settings.MEDIA_ROOT) + '/' + str(filename)
        wb = load_workbook(path)
        sheet = wb.worksheets[0]

        data, isFirst = [], True
        for row in sheet.rows:
            if isFirst:
                isFirst = False
                continue
            tmp = {}
            tmp['name'] = row[0].value 
            tmp['detail'] = row[1].value 
            tmp['count'] = row[2].value 
            tmp['status'] = row[3].value 
            data.append(tmp)
        
        voteTargetOp = VoteTargetOp()
        voteTargetList = []
        for voteTarget in data:
            ok, msg = voteTargetOp.checkDataOnCreateMany(voteTarget['name'], voteTarget['detail'], voteId, voteTarget['count'], voteTarget['status'])
            if ok:
                voteTargetList.append(models.VoteTarget(
                    name = voteTarget['name'],
                    detail = voteTarget['detail'],
                    vote_id_id = voteId,
                    count = voteTarget['count'],
                    status = voteTarget['status'],
                ))
                # voteTargetOp.create(voteTarget)
            else:
                message = msg
        if message == 'success':
            models.VoteTarget.objects.bulk_create(voteTargetList)

    except Exception as e:
        message = str(e)

    status = 1 if message == 'success' else 2
    TaskOp().updateStatus(taskId, status, message)
    # models.Task.objects.filter(task_id=taskId).update(
    #     status = 1 if message == 'success' else 2,
    #     msg = message
    # )
    