import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from tools import genearteMD5, getNowTimeStamp, Validate

class User(APIView):
    def __init__(self):
        self.ERROR1 = 'username or password error'

    def post(self, request, *arg, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            username = json.loads(request.body).get('username', None)
            pwd = json.loads(request.body).get('pwd', None)
            ok, data = self.login(username, pwd)
            if ok:
                ret['user_data'] = serializers.serialize('json', data)
            else:
                ret['code'] = 400
                ret['msg'] = data
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
        return ret

    def onLoginSuccess(self, userObj):
        userObj.last_login_time = getNowTimeStamp()
        userObj.save()

    def login(self, username, pwd):
        pwdMD5 = genearteMD5(pwd)
        if not self.checkUsernameExist(username):
            return False, self.ERROR1
        userObj = models.User.objects.get(usrname=username)
        if pwdMD5 == userObj.pwd:
            self.onLogin(userObj)
            return True, userObj
        else:
            return False, self.ERROR1

    def checkUsernameExist(self, username):
        userObj = models.User.objects.filter(username=username)
        return userObj.exists()
    
    def onRegisterSuccess():
        pass

    def checkData(self, userdata):
        name = userdata.name
        username = userdata.username
        pwd = userdata.pwd
        email = userdata.email
        auth = userdata.auth
        acator = userdata.acator
        if self.checkUsernameExist(username):
            return False, self.ERROR1
        if Validate.isEmpty(name):
            return False, 'name cannot be empty'
        if Validate.isEmpty(pwd):
            return False, 'password cannot be empty'
        if Validate.isEmpty(email) or Validate.isEmail(email):
            return False, 'email error'
        if auth not in [0, 1]:
            return False, 'auth error'
        return True, None
        

    def register(self, userdata):
        ok, res = self.checkData(userdata)
        if not ok:
            return False, res
        pwdMD5 = genearteMD5(userdata.pwd)
        userdata.nowTime = getNowTimeStamp()
        
