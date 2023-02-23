import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.views.UserOp import UserOp


class SendEmailCode(APIView):
    def post(self, request, *arg, **kwargs):
        ret = {'code': 200, "msg": 'ok'}
        try:
            email = json.loads(request.body).get('email', None) 
            userop = UserOp()
            ok, msg = userop.checkEmail(email)
            if not ok:
                return JsonResponse({'code': 400, "msg": msg})
            ok, msg = userop.checkEmailExist(email)
            if ok:
                return JsonResponse({'code': 400, "msg": 'email is already exists'})
            ok, msg = userop.sendEmail(email)
            if not ok:
                return JsonResponse({'code': 400, "msg": msg})
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)