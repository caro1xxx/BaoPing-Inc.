import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.tools import genearteMD5, getNowTimeStamp, Validate, generateString16, generateCode6
from django.core.mail import send_mail
from vote_manage import settings

class UserOp:
    def __init__(self):
        self.ERROR1 = 'username or password error'
            
    def onLoginSuccess(self, userObj):
        userObj.last_login_time = getNowTimeStamp()
        userObj.save()

    def login(self, username, pwd):
        pwdMD5 = genearteMD5(pwd)
        if not self.checkUsernameExist(username):
            return False, self.ERROR1
        userObj = models.User.objects.get(username=username)
        # print(pwd, pwdMD5, userObj.pwd)
        if pwdMD5 == userObj.pwd:
            self.onLoginSuccess(userObj)
            return True, userObj
        else:
            return False, self.ERROR1

    def checkUsernameExist(self, username):
        userObj = models.User.objects.filter(username=username)
        return userObj.exists(), 'username already exists'
    
    def checkName(self, name):
        validate = Validate()
        validate.addCheck('checkMinLength', name, 'name min length is 2', 2)
        validate.addCheck('checkMaxLength', name, 'name max length is 8', 8)
        validate.addCheck('checkHasNoSpace', name, 'name has space')
        return validate.startCheck()

    def checkUsername(self, username):
        validate = Validate()
        validate.addCheck('checkMinLength', username, 'username min length is 5', 5)
        validate.addCheck('checkMaxLength', username, 'username max length is 8', 8)
        validate.addCheck('checkHasNoSpace', username, 'username has space')
        validate.addCheck('checkOnlyNumal', username, 'username only number and alapha')
        return validate.startCheck()

    def checkEmail(self, email):
        validate = Validate()
        validate.addCheck('checkMinLength', email, 'email min length is 5', 5)
        validate.addCheck('checkMaxLength', email, 'email max length is 20', 20)
        validate.addCheck('checkHasNoSpace', email, 'email has space')
        validate.addCheck('checkIsEmail', email, 'is not a email')
        return validate.startCheck()

    def checkEmailExist(self, email):
        userObj = models.User.objects.filter(email=email)
        return userObj.exists(), 'email already exists'

    def checkPwd(self, pwd):
        print("check validate pwd")
        validate = Validate()
        validate.addCheck('checkMinLength', pwd, 'password min length is 8', 8)
        validate.addCheck('checkMaxLength', pwd, 'password max length is 16', 16)
        validate.addCheck('checkHasNoSpace', pwd, 'password has space')
        ok, res = validate.startCheck()
        return ok, res
        return validate.startCheck()
    
    def checkAuth(self, auth):
        if auth not in [0, 1]:
            return False, 'auth error'
        return True, None
    
    def checkData(self, userdata):
        ok, msg = self.checkUsernameExist(userdata['username'])
        if ok:
            return False, 'username repeat'
        ok, msg = self.checkName(userdata['name'])
        if not ok:
            return ok, msg
        ok, msg = self.checkPwd(userdata['pwd'])
        if not ok:
            return ok, msg
        ok, msg = self.checkEmail(userdata['email'])
        if not ok:
            return ok, msg
        ok, msg = self.checkEmailExist(userdata['email'])
        if ok:
            return False, msg
        ok, msg = self.checkEmailCode(userdata['email'], userdata['email_code'])
        if not ok:
            return ok, msg
        return True, None

    def onRegisterSuccess(self):
        pass    

    def register(self, userdata):
        try:
            ok, msg = self.checkData(userdata)
            if not ok:
                return False, msg
            userdata['pwd'] = genearteMD5(userdata['pwd'])
            userdata['create_time'] = getNowTimeStamp()
            userdata['last_login_time'] = getNowTimeStamp()
            userdata['auth'] = 1
            userdata['avator'] = userdata.get('avator', '/static/img/avator/avator1.jpeg')
            userdata['token'] = generateString16()
            userdata['status'] = 1
            userObj = models.User.objects.create(name = userdata['name'], username = userdata['username'], pwd= userdata['pwd'], create_time = userdata['create_time'], last_login_time = userdata['last_login_time'], email = userdata['email'], auth = userdata['auth'], avator = userdata['avator'], token = userdata['token'], status = userdata['status'])
            userObj.save()
            return True, None
        except Exception as e:
            return False, str(e)
            return False, 'Timeout'
            
    def sendEmail(self, email):
        try:
            code = generateCode6()
            content = code
            my_email = send_mail('你的验证码是:{}'.format(email), content, settings.DEFAULT_FROM_EMAIL, [email])
            if my_email != 1:
                return False, 'send email error'
            key = 'syl_' + email
            cache.set(key, code, 300)  
        except Exception as e:
            return False, 'send email code error'
        return True, 'send email code success'
    
    def checkEmailCode(self, email, emailCode):
        try:
            userop = UserOp()
            ok, msg = userop.checkEmail(email)
            if not ok:
                return ok, msg
            if emailCode is None:
                return ok, 'code is empty'

            serverEmailCode = cache.get('syl_' + email, None)
            print(emailCode, serverEmailCode)
            if serverEmailCode is None:
                return ok, 'code timetout'
            cache.delete('syl_' + email)
            if serverEmailCode != emailCode:
                return ok, 'code error'
        except Exception as e:
            return False, 'Timeout'
        return True, None



