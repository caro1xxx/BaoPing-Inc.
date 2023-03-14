from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.views.support.SupportOp import SupportOp
from main.views.keys.KeysOp import KeysOp
from main.tools import getNowTimeStamp, getIp
import json
from main.tools import getIp


class Support(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '添加成功'}
        try:
            data = json.loads(request.body).get('data', None)

            ok, msg = SupportOp().checkDataOnCreate(data)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            
            # ok, msg = KeysOp().checkKey(data['key'])
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})

            data['ip'] = getIp(request)
            ok, msg = SupportOp().checkSettingsOnCreate(data)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})

            SupportOp().create(data, request)
            ret['data'] = "{}"

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)