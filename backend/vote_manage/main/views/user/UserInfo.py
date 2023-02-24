import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.views.user.UserOp import UserOp


class UserInfo(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            username = request.GET.get('username', None)

            userOp = UserOp()
            ok, msg = userOp.checkUsername(username)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            ok, msg = userOp.checkUsernameExist(username)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            
            ret['data'] = serializers.serialize("json", models.User.objects.filter(username=username))
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
        return JsonResponse(ret)
        

    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            pass
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
        return JsonResponse(ret)

    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            pass
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
        return JsonResponse(ret)

    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            pass
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
        return JsonResponse(ret)