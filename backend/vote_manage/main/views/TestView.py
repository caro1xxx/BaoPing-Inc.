from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import generateCode6
import json
from main.tools import Validate
from main.views.vote_activity.VoteActivityOp import VoteActivityOp
from django.core.paginator import Paginator
from vote_manage.settings import BASE_DIR
import geoip2.database
from vote_manage import settings
from main.tasks import myTask, sendEmail
from vote_manage import settings
from openpyxl import load_workbook
from main.views.vote_target.VoteTargetOp import VoteTargetOp


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        ret = {}
        try:
            myTask.delay()
            sendEmail.delay('isliliyu@gmail.com')
            ret['msg'] = 'success'
        except Exception as e:
            ret['msg'] = str(e)

        return JsonResponse(ret)
    
    def post(self, request, *args, **kwargs):
        ret = {'code': 200}
        try:
            file = request.FILES.get('file', None)

            models.TempFile.objects.create(file=file)
            path = str(settings.MEDIA_ROOT) + '/temp/' + file.name
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
                ok, msg = voteTargetOp.checkData(voteTarget)
                if ok:
                    voteTargetOp.create(data)


        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'msg': str(e)}
        return JsonResponse(ret)