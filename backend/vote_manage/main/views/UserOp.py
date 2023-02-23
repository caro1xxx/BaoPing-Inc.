import json
from main import models
from django.core.cache import cache
from main.tools import genearteMD5, getNowTimeStamp, Validate, generateString16, generateCode6, b64Encode, b64Decode
from django.core.mail import send_mail
from vote_manage import settings


# 关于用户的一些操作
class UserOp:
    def __init__(self):
        self.ERROR1 = '用户名或密码错误'
            
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

    # 检查username是否已经注册
    def checkUsernameExist(self, username):
        userObj = models.User.objects.filter(username=username)
        return userObj.exists(), '用户名已注册'
    
    # 验证用户姓名的格式是否正确
    def checkName(self, name):
        validate = Validate()
        validate.addCheck('checkMinLength', name, '姓名最小长度为2', 2)
        validate.addCheck('checkMaxLength', name, '姓名最大长度为8', 8)
        validate.addCheck('checkHasNoSpace', name, '姓名不能包含空格')
        return validate.startCheck()

    #  验证用户名格式是否正确
    def checkUsername(self, username):
        validate = Validate()
        validate.addCheck('checkMinLength', username, '用户名最小长度为5', 5)
        validate.addCheck('checkMaxLength', username, '用户名最大长度为8', 8)
        validate.addCheck('checkHasNoSpace', username, '用户名不能包含空格')
        validate.addCheck('checkOnlyNumal', username, '用户名只支持数字和字母的组合')
        return validate.startCheck()
    
    # 验证email格式是否正确
    def checkEmail(self, email):
        validate = Validate()
        validate.addCheck('checkMinLength', email, '邮箱最小长度为5', 5)
        validate.addCheck('checkMaxLength', email, '邮箱最大长度为20', 20)
        validate.addCheck('checkHasNoSpace', email, '邮箱不能包含空格')
        validate.addCheck('checkIsEmail', email, '邮箱格式错误')
        return validate.startCheck()

    # 检查email是否已经注册
    def checkEmailExist(self, email):
        userObj = models.User.objects.filter(email=email)
        return userObj.exists(), '邮箱已经注册'

    # 验证密码格式是否正确
    def checkPwd(self, pwd):
        print("check validate pwd")
        validate = Validate()
        validate.addCheck('checkMinLength', pwd, '密码最小长度为8', 8)
        validate.addCheck('checkMaxLength', pwd, '密码最大长度为16', 16)
        validate.addCheck('checkHasNoSpace', pwd, '密码不能包含空格')
        ok, res = validate.startCheck()
        return ok, res
    
    def checkData(self, userdata):
        ok, msg = self.checkUsernameExist(userdata['username'])
        if ok:
            return False, '用户名重复'
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

    def generatreToken(self, username):
        data = username + ' ' + str(getNowTimeStamp())
        data = b64Encode(data)
        return data

    def getDataFromToken(self, token):
        data = b64Decode(token)
        usrename, lastLoginTime = data.split(' ')
        lastLoginTime = int(lastLoginTime)
        return usrename, lastLoginTime

    def onRegisterSuccess(self):
        pass    

    def register(self, userdata, request):
        try:
            ok, msg = self.checkData(userdata)
            if not ok:
                return False, msg
            userdata['pwd'] = genearteMD5(userdata['pwd'])
            userdata['create_time'] = getNowTimeStamp()
            userdata['last_login_time'] = getNowTimeStamp()
            userdata['auth'] = 1
            userdata['avator'] = request.FILES.get('avator', None)  
            if userdata['avator'] is None:
                return False, '头像地址错误'
            # userdata['avator'] = userdata.get('avator', '/static/img/avator/avator1.jpeg')
            # userdata['token'] = generateString16()
            userdata['token'] = self.generatreToken(userdata['username'])
            userdata['status'] = 1
            userObj = models.User.objects.create(name = userdata['name'], username = userdata['username'], pwd= userdata['pwd'], create_time = userdata['create_time'], last_login_time = userdata['last_login_time'], email = userdata['email'], auth = userdata['auth'], avator = userdata['avator'], token = userdata['token'], status = userdata['status'])
            userObj.save()
            return True, None
        except Exception as e:
            # return False, str(e)
            return False, 'Timeout'
            
    def sendEmail(self, email):
        try:
            code = generateCode6()
            content = code
            my_email = send_mail('你的验证码是:{}'.format(email), content, settings.DEFAULT_FROM_EMAIL, [email])
            if my_email != 1:
                return False, '发送验证码失败'
            key = 'syl_' + email
            cache.set(key, code, 300)  
        except Exception as e:
            return False, '发送验证码失败'
        return True, '发送验证码成功'
    
    def checkEmailCode(self, email, emailCode):
        try:
            userop = UserOp()
            ok, msg = userop.checkEmail(email)
            if not ok:
                return ok, msg
            if emailCode is None:
                return ok, '验证码不能为空'

            serverEmailCode = cache.get('syl_' + email, None)
            print(emailCode, serverEmailCode)
            if serverEmailCode is None:
                return ok, '验证码已过期'
            cache.delete('syl_' + email)
            if serverEmailCode != emailCode:
                return ok, '验证码错误'
        except Exception as e:
            return False, 'Timeout'
        return True, None




