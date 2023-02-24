import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.tools import genearteMD5, getNowTimeStamp, Validate
from main.views.user.UserOp import UserOp


# 注册用户，先验证用户资料再验证邮件验证码
class Register(APIView):
    def post(self, request, *ary, **kwargs):
        ret = {'code': 200, 'msg': '注册成功'}
        try:
            userdata = json.loads(request.body).get("data", None)
            # userdata = json.loads(request.body).get('data', None)
            if not Validate().checkIsNotEmpty(userdata):
                ret = {'code': 404, 'msg': '没有用户数据'}
                return JsonResponse(ret)
            userOp = UserOp()
            ok, msg = userOp.register(userdata, request)
            if not ok:
                ret = {'code': 400, 'msg': msg}
            ret['data'] = serializers.serialize("json",models.User.objects.filter(username=userdata['username']))
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)