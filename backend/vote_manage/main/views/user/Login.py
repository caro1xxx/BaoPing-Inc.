import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.views.user.UserOp import UserOp


class Login(APIView):
    def get(self, request, *arg, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            token = request.GET.get('token', None)
            userOp = UserOp()
            ok, data = userOp.loginWithToken(token)
            if ok:
                ret['data'] = serializers.serialize("json",models.User.objects.filter(username=data.username))
            else:
                ret['code'] = 400
                ret['msg'] = data
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    def post(self, request, *arg, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            username = json.loads(request.body).get('username', None)
            pwd = json.loads(request.body).get('pwd', None)
            userOp = UserOp()
            ok, data = userOp.login(username, pwd)
            if ok:
                ret['data'] = serializers.serialize("json",models.User.objects.filter(username=data.username))
            else:
                ret['code'] = 400
                ret['msg'] = data
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)