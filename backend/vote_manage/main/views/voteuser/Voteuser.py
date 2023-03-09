import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.views.user.UserOp import UserOp
from main.tools import *
from main.views.Common import Common


class Voteuser(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            # username = request.GET.get('username', None)
            # data = models.VoteUser.objects.all()
            # data, ret['page_count'] = myPaginator(data, 10, request.GET.get('page_num', 1))
            # ret['data'] = serializers.serialize('json', data, use_natural_foreign_keys=True)
            ret['data'], ret['page_count'] = Common().getData(request, 'VoteUser', maxsize=20)
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)