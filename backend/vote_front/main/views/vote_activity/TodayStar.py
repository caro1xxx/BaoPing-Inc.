from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import generateCode6, myPaginator
import json
from main.tools import Validate
from django.db.models import F


class TodayStar(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            voteId = request.GET.get('vote_id', None)
            voteObj = models.VoteActivity.objects.filter(vote_id=voteId).first()
            if voteObj is None:
                return JsonResponse({'code': 400, 'msg': '活动不存在'})
            
            todayStar = voteObj.today_start_voteuser
            if todayStar in ['', None]:
                return JsonResponse({'code': 400, 'msg': '暂无今日之星'})

            voteuserObj = models.VoteTarget.objects.filter(pk=todayStar).first()
            if voteuserObj is None:
                return JsonResponse({'code': 400, 'msg': '今日之星不存在'})

            ret['data'] = serializers.serialize('json', [voteuserObj])

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'msg': str(e)}
        return JsonResponse(ret)