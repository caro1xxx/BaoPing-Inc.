from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import getNoWTimeStamp
import json


class Token(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            info = request.GET.get('info', None)

            config = models.OfficialAccount.objects.all().first()

            if info in [None, 'base']:
                ret['token'] = config.access_token_value
            else:
4                ret['token'] = config.access_token_advanced_value

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            data = json.loads(request.body).get('data', None)
            info = data.get('info', None)
            value = data.get('token_value', None)
            expireTime = data.get('expire_time', None)

            config = models.OfficialAccount.objects.all().first()

            if info in [None, 'base']:
                config.access_token_value = value
                config.access_token_expire_time = expireTime
            else:
                config.access_token_advanced_value = value
                config.access_token_advanced_expire_time = expireTime

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)