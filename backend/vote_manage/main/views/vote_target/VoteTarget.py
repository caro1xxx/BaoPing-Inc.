from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
import json
from main.tools import *
from django.core.paginator import Paginator
from main.views.vote_target.VoteTargetOp import VoteTargetOp


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
            count = request.POST.get('count', None)
            
            ok, msg = VoteTargetOp().checkData(detail, name, voteId, count)
            if not ok:
                return msg

            models.VoteTarget.objects.create(
                detail = detail,
                name = name,
                avator = avator,
                vote_id_id = voteId,
                count = count
            ).save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}

        return JsonResponse(ret)
    
    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            pk = json.loads(request.body).get('userId', None)
            name = json.loads(request.body).get('name', None)
            detail = json.loads(request.body).get('detail', None)
            count = json.loads(request.body).get('count', None)
            status = json.loads(request.body).get('status', None)

            ok, msg = VoteTargetOp().checkDataOnUpdate(name, detail, count, pk)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})

            voteTargetObj = models.VoteTarget.objects.filter(pk=pk).first()
            if voteTargetObj is None:
                return JsonResponse({'code': 400, 'msg': 'not found'})
            
            voteTargetObj.name = name
            voteTargetObj.detail = detail
            voteTargetObj.count = count
            voteTargetObj.status = status
            voteTargetObj.save()
        
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}

        return JsonResponse(ret)