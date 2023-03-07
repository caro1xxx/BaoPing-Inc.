from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import getNowTimeStamp
from main.views.voteuser.VoteUserOp import VoteUserOp
import json


class VoteUser(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '添加成功'}
        try:
            data = json.loads(request.body).get('data', None)

            ok, msg = VoteUserOp().checkDataOnCreate(
                data.get('open_id', None),
                data.get('wx_username', None),
                data.get('avator', None),
            )
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})

            models.VoteUser.objects.create(
                open_id = data['open_id'],
                wx_username = data['wx_username'],
                create_time = getNowTimeStamp(),
                avator = data['avator'],
            ).save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)