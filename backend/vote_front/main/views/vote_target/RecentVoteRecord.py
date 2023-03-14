from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from django.db.models import F, Q
from main.tools import getNowTimeStamp, getIp
import json
from main.tools import myPaginator


class RecentFiveVoteRecord(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            voteId = request.GET.get('vote_id', None)
            voteTargetId = request.GET.get('vote_target_id', None)
            
            data = models.VoteRecord.objects.filter(
                vote_activity = voteId,
                vote_target_id = voteTargetId
            ).order_by('-pk')[:5]
            ret['data'] = serializers.serialize('json', data, use_natural_foreign_keys=True)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)