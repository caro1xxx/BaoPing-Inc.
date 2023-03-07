from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import generateCode6, myPaginator
import json
from main.tools import Validate


class AloneVoteActivity(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            voteId = request.GET.get('vote_id', None)
            voteObj = models.VoteActivity.objects.filter(vote_id=voteId).first()
            if voteObj is None:
                return JsonResponse({'code': 400, 'msg': 'not found'})
            
            ret['data'] = serializers.serialize('json', [voteObj])

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'msg': str(e)}
        return JsonResponse(ret)