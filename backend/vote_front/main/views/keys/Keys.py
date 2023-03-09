from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from django.db.models import F
from main.views.support.SupportOp import SupportOp
from main.tools import getNowTimeStamp, getIp
import json
from main.views.keys.KeysOp import KeysOp
import base64


class Keys(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '添加成功'}
        try:
            openId = request.GET.get('open_id', None)

            keysOp = KeysOp()
            ok, msg = keysOp.checkDataOnCreate(openId)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            
            keysObj = keysOp.create(openId)
            ret['key'] = keysObj.value
            ret['data'] = "{}"
            # ret['base64key'] = base64.b64encode((ret['key'] + 'vote').encode(encoding='utf-8')).decode()
            # ret['decodekey'] = base64.b64decode(ret['base64key'].encode()).decode().replace('vote', '')

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)