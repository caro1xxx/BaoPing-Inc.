from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
import json
from main.tools import *
from django.core.paginator import Paginator
from main.views.vote_target.VoteTargetOp import VoteTargetOp


class UpdateVoteTargetStatus(APIView):
    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            data = json.loads(request.body).get('data', None)
            if data is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})

            voteTargetObj = models.VoteTarget.objects.filter(pk=data['pk']).first()
            if voteTargetObj is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})

            voteTargetObj.status = data['status']
            voteTargetObj.save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)