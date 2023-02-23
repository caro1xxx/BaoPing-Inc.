import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.views.UserOp import UserOp


class CheckEmailCode(APIView):
    def post(self, request, *arg, **kwargs):
        ret = {'code': 200, "msg": 'ok'}
        try:
            email = json.loads(request.body).get('email', None) 
            emailCode = json.loads(request.body).get('email_code', None) 
            userop = UserOp()
            ok, msg = userop.checkEmail(email)
            if not ok:
                return JsonResponse({'code': 400, "msg": msg})
            if emailCode is None:
                return JsonResponse({'code': 400, "msg": 'code is empty'})

            serverEmailCode = cache.get('syl_' + email, None)
            print(emailCode, serverEmailCode)
            if serverEmailCode is None:
                return JsonResponse({'code': 400, "msg": 'code timetout'})
            cache.delete('syl_' + email)
            if serverEmailCode != emailCode:
                ret = JsonResponse({'code': 400, "msg": 'code error'})
                return ret
        except Exception as e:
            return JsonResponse({'code': 500, 'msg': 'Timeout'})
        return JsonResponse(ret)