from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import getNoWTimeStamp
import json


class CheckTokenExpireTime(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            info = request.GET.get('info', None)

            config = models.OfficialAccount.objects.all().first()

            if info in [None, 'base']:
                ret['data'] = config.access_token_expire_time >= getNoWTimeStamp()
            else:
                ret['data'] = config.access_token_advanced_expire_time >= getNoWTimeStamp()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)