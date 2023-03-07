from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from django.db.models import F
from main.views.support.SupportOp import SupportOp
from main.tools import getNowTimeStamp, getIp
import json
from main.views.vote_target.VoteTargetOp import VoteTargetOp
from main.tools import myPaginator


class VoteTarget(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            voteId = request.GET.get('vote_id', None)
            if voteId is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})
            
            voteTargetObj = models.VoteTarget.objects.filter(vote_id=voteId)
            if voteTargetObj is None:
                return JsonResponse({'code': 400, 'msg': 'not found'})

            data = voteTargetObj
            data, ret['page_count'] = myPaginator(data, 10, request.GET.get('page_num', 1))
            ret['data'] = serializers.serialize('json', voteTargetObj)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
    
    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '添加成功'}
        try:
            detail = request.POST.get('detail', None)
            name = request.POST.get('name', None)
            avator = request.FILES.get('avator', None)
            voteId = request.POST.get('vote_id', None)
            
            ok, msg = VoteTargetOp().checkDataOnCreate(detail, name, voteId)
            if not ok:
                return msg

            models.VoteTarget.objects.create(
                detail = detail,
                name = name,
                avator = avator,
                vote_id_id = voteId,
            ).save()
            

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)