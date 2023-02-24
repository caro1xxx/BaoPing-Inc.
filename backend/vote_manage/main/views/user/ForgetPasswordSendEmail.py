import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.views.user.UserOp import UserOp


# 忘记密码时使用的发送邮件接口，如果邮箱未注册会报错
class ForgetPasswordSendEmail(APIView):
    def post(self, request, *arg, **kwargs):
        ret = {'code': 200, "msg": '发送成功'}
        try:
            email = json.loads(request.body).get('email', None) 
            userop = UserOp()
            ok, msg = userop.checkEmail(email)
            if not ok:
                return JsonResponse({'code': 400, "msg": msg})
            ok, msg = userop.checkEmailExist(email)
            if not ok:
                return JsonResponse({'code': 400, "msg": '邮箱未注册'})
            ok, msg = userop.sendEmail(email)
            if not ok:
                return JsonResponse({'code': 400, "msg": msg})
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)