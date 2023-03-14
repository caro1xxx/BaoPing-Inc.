import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache


class RecentVoteRecord(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            open_id = request.GET.get('open_id', None)
            
            if open_id is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})

            voteRecordObj = models.VoteRecord.objects.filter(voteuser_id=open_id).order_by('-create_time').first()
            ret['data'] = serializers.serialize('json', [voteRecordObj]) if voteRecordObj else '[]'
            
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
