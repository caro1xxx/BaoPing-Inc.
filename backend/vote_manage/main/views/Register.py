import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.tools import genearteMD5, getNowTimeStamp, Validate
from main.views.UserOp import UserOp


class Register(APIView):
    def post(self, request, *ary, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            userdata = json.loads(request.body).get('data', None)
            if not Validate().checkIsNotEmpty(userdata):
                ret = {'code': 404, 'msg': 'no userdata'}
                return JsonResponse(ret)
            userOp = UserOp()
            ok, msg = userOp.register(userdata)
            if not ok:
                ret = {'code': 400, 'msg': msg}
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)