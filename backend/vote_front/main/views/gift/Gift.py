from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import getNowTimeStamp, myPaginator
import json


class Gift(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            voteId = request.GET.get('vote_id', None)
            
            if voteId is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})

            voteActivityObj = models.VoteActivity.objects.filter(vote_id=voteId).first()
            if voteActivityObj is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})

            if voteActivityObj.enable_prize == 0:
                ret['data'] = '{}'
            else:
                data = models.Gift.objects.filter(status=1)
                data, ret['page_count'] =  myPaginator(data, 20)
                ret['data'] = serializers.serialize('json', data)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)