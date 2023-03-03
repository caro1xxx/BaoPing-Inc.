from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import *
from main.views.Common import Common
import json


class Settings(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            ret['data'], ret['page_count'] = Common().getData(request, 'Settings', maxsize=20)
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
    
    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            pk = json.loads(request.body).get('pk', None)
            value = json.loads(request.body).get('value', 0)

            if pk is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})

            settingsObj = models.Settings.objects.filter(pk=pk).first()
            if settingsObj is None:
                return JsonResponse({'code': 400, 'msg': '没有该设置项'})
            settingsObj.value = value
            settingsObj.save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)