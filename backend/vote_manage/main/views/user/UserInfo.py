import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.views.user.UserOp import UserOp
from main.tools import *


class UserInfo(APIView):
    # 获取全部用户信息
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            # username = request.GET.get('username', None)
            ret['data'] = serializers.serialize("json", models.User.objects.all())
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
        return JsonResponse(ret)
        
    # 新增一条用户信息
    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '创建成功'}
        try:
            userdata = json.loads(request.body).get('data', None)
            ok, msg = UserOp().checkData(userdata)
            if not ok:
                return JsonResponse({"code": 400, "msg": msg})
            
            userdata['pwd'] = genearteMD5(userdata['pwd'])
            userdata['create_time'] = getNowTimeStamp()
            userdata['last_login_time'] = 0
            userdata['token'] = '-'

            userObj = models.User.objects.create(name = userdata['name'], username = userdata['username'], pwd=userdata['pwd'], create_time = userdata['create_time'], last_login_time = userdata['last_login_time'], email = userdata['email'], auth = userdata['auth'], avator = userdata['avator'], token = userdata['token'], status = userdata['status'])
            userObj.save()
        
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    # 修改用户信息
    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            # userdata = json.loads(str(request.body, encoding='utf-8')).get('data', None)
            userdata = json.loads(request.body).get('data', None)

            ok, msg = UserOp().checkDataOnUpdate(userdata)
            if not ok:
                return JsonResponse({"code": 400, "msg": msg})
            
            userObj = models.User.objects.get(username=userdata['username'])
            userObj.name = userdata['name']
            userObj.auth = userdata['auth']
            userObj.pwd = genearteMD5(userdata['pwd'])
            userObj.status = userdata['status']
            userObj.save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    # 删除用户信息
    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '删除成功'}
        try:
            username = json.loads(request.body).get('username', None)
            # 校验username
            models.User.objects.filter(username=username).delete()
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
        return JsonResponse(ret)