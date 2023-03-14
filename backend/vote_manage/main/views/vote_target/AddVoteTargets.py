from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
import json
from main.tools import *
from django.core.paginator import Paginator
from main.views.vote_target.VoteTargetOp import VoteTargetOp
from openpyxl import load_workbook
from vote_manage import settings
from main.tasks import addVoteTargets
from main.views.task.TaskOp import TaskOp


# 批量添加选手，上传一个excel文件，只有通过验证的数据才会添加，并且不会提示错误信息
class AddVoteTargets(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '上传成功'}
        try:
            file = request.FILES.get('file', None)
            voteId = request.POST.get('vote_id', None)
            fileObj = models.TempFile.objects.create(file=file)
            
            # voteTargetOp = VoteTargetOp()
            # voteTargetList = []
            # for voteTarget in data:
            #     ok, msg = voteTargetOp.checkData(voteTarget['name'], voteTarget['detail'], voteTarget['vote_id'], voteTarget['count'])
            #     if not ok:
            #         return JsonResponse({'code': 400, 'msg': msg})
            #     voteTargetList.append(models.VoteTarget(
            #         name = voteTarget['name'],
            #         detail = voteTarget['detail'],
            #         vote_id = voteTarget['vote_id'],
            #         count = voteTarget['count'],
            #         status = voteTarget['status'],
            #     ))
            # taskId = generateCode6()
            # models.Task.objects.create(
            #     task_id = taskId,
            #     name = 'addvoteTargets',
            #     status = 0,
            #     msg = ''
            # )
            taskId = TaskOp().create('批量添加选手')
            ret['task_id'] = taskId
            addVoteTargets.delay(str(fileObj.file), taskId, voteId)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}

        return JsonResponse(ret)