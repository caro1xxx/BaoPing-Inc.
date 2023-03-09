from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
import json
from main.tools import *
from django.core.paginator import Paginator
from main.views.vote_target.VoteTargetOp import VoteTargetOp
from openpyxl import load_workbook


# 批量添加选手，上传一个excel文件，只有通过验证的数据才会添加，并且不会提示错误信息
class AddVoteTargets(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '添加成功'}
        try:
            file = request.FILES.get('file', None)

            fileObj = models.TempFile.objects.create(file=file)
            path = str(settings.MEDIA_ROOT) + '/' + str(fileObj.file)
            print(path)
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

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'?code': 500, 'msg': 'Timeout', 'error': str(e)}

        return JsonResponse(ret)