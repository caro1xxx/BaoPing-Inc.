import json
from main import models
from django.core.cache import cache
from main.tools import genearteMD5, getNowTimeStamp, Validate, generateString16, generateCode6, b64Encode, b64Decode
from django.core.mail import send_mail
from vote_manage import settings
from main.tools import *
import base64


# 关于用户的一些操作
class UserOp:
    def __init__(self):
        self.ERROR1 = '用户名或密码错误'
            
    def onLoginSuccess(self, userObj):
        token = userObj.token
        userObj.last_login_time = getNowTimeStamp()
        userObj.token = self.generatreToken(userObj.username)
        userObj.save()
        # 登陆成功删除旧token
        tokenObj = models.Token.objects.filter(value=token).first()
        if tokenObj:
            tokenObj.delete()

    def loginWithToken(self, token):
        userObj = models.User.objects.filter(token=token).first()
        if userObj:
            self.onLoginSuccess(userObj)
            return True, userObj
        else:
            return False, 'token已过期'

    def login(self, username, pwd):
        pwdMD5 = genearteMD5(pwd)
        ok, msg = self.checkUsername(username)
        if not ok:
            return False, msg
        ok, msg = self.checkUsernameExist(username)
        if not ok:
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
        if userObj.exists():
            return True, '用户名已注册'
        return False, '用户名不存在'
    
    # 验证用户姓名的格式是否正确
    def checkName(self, name):
        validate = Validate()
        validate.addCheck('checkMinLength', name, '姓名最小长度为2', 2)
        validate.addCheck('checkMaxLength', name, '姓名最大长度为8', 8)
        validate.addCheck('checkHasNoSpace', name, '姓名不能包含空格')
        ok, msg = validate.startCheck()
        return ok, msg

    #  验证用户名格式是否正确
    def checkUsername(self, username):
        validate = Validate()
        validate.addCheck('checkMinLength', username, '用户名最小长度为5', 5)
        validate.addCheck('checkMaxLength', username, '用户名最大长度为8', 8)
        validate.addCheck('checkHasNoSpace', username, '用户名不能包含空格')
        validate.addCheck('checkOnlyNumal', username, '用户名只支持数字和字母的组合')
        ok, msg = validate.startCheck()
        return ok, msg
    
    # 验证email格式是否正确
    def checkEmail(self, email):
        validate = Validate()
        validate.addCheck('checkMinLength', email, '邮箱最小长度为5', 5)
        validate.addCheck('checkMaxLength', email, '邮箱最大长度为20', 20)
        validate.addCheck('checkHasNoSpace', email, '邮箱不能包含空格')
        validate.addCheck('checkIsEmail', email, '邮箱格式错误')
        ok, msg = validate.startCheck()
        return ok, msg

    # 检查email是否已经注册
    def checkEmailExist(self, email):
        userObj = models.User.objects.filter(email=email)
        return userObj.exists(), '邮箱已经注册'

    # 验证密码格式是否正确
    def checkPwd(self, pwd):
        validate = Validate()
        validate.addCheck('checkMinLength', pwd, '密码最小长度为8', 8)
        validate.addCheck('checkMaxLength', pwd, '密码最大长度为16', 16)
        validate.addCheck('checkHasNoSpace', pwd, '密码不能包含空格')
        ok, msg = validate.startCheck()
        return ok, msg
    
    # 检查auth格式是否正确
    def checkAuth(self, auth):
        if auth is None:
            return False, 'auth error'
        return int(auth) in [0, 1], 'auth error'
    
    # 检查状态格式是否正确
    def checkStatus(self, status):
        if status is None:
            return False, 'status error'
        return int(status) in [0, 1], 'status error'
    
    # 当更新用户的时候检查数据
    def checkDataOnUpdate(self, userdata):
        ok, msg = self.checkUsername(userdata['username'])
        if not ok:
            return False, msg
        ok, msg = self.checkUsernameExist(userdata['username'])
        if not ok:
            return False, '用户名不存在'
        ok, msg = self.checkName(userdata['name'])
        if not ok:
            return ok, msg
        ok, msg = self.checkPwd(userdata['pwd'])
        if not ok:
            return ok, msg
        ok, msg = self.checkAuth(userdata['auth'])
        if not ok:
            return ok, msg
        ok, msg = self.checkStatus(userdata['status'])
        if not ok:
            return ok, msg
        if userdata.get('email_code', None):
            ok, msg = self.checkEmailCode(userdata['email'], userdata['email_code'])
            if not ok:
                return ok, msg
        return True, None

    # 验证用户数据是否正确
    def checkData(self, userdata):
        ok, msg = self.checkUsername(userdata['username'])
        if not ok:
            return False, msg
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
        if userdata.get('email_code', None):
            ok, msg = self.checkEmailCode(userdata['email'], userdata['email_code'])
            if not ok:
                return ok, msg
        return True, None

    # 根据用户名和当前时间戳生成加密token
    def generatreToken(self, username):
        token = generateString32()
        expire_time = getNowTimeStamp() + (7 * 24 * 60 * 60)
        tokenModels = models.Token.objects.create(value=token, expire_time=expire_time)
        tokenModels.save()
        return token

    def onRegisterSuccess(self):
        pass    

    # 注册用户
    def register(self, userdata, request):
        try:
            ok, msg = self.checkData(userdata)
            if not ok:
                return False, msg
            userdata['pwd'] = genearteMD5(userdata['pwd'])
            userdata['create_time'] = getNowTimeStamp()
            userdata['last_login_time'] = getNowTimeStamp()
            userdata['auth'] = 1
            userdata['token'] = self.generatreToken(userdata['username'])
            userdata['status'] = 1
            userObj = models.User.objects.create(
                name = userdata['name'],
                username = userdata['username'], 
                pwd= userdata['pwd'], 
                create_time = userdata['create_time'], 
                last_login_time = userdata['last_login_time'], 
                email = userdata['email'], 
                auth = userdata['auth'], 
                avator = userdata['avator'], 
                token = userdata['token'], 
                status = userdata['status']
            )
            userObj.save()
            return True, None
        except Exception as e:
            # return False, str(e)
            return False, 'Timeout'
    
    # 发送六位数字验证码到邮箱
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
    
    # 检查验证码是否正确
    def checkEmailCode(self, email, emailCode):
        try:
            userop = UserOp()
            ok, msg = userop.checkEmail(email)
            if not ok:
                return ok, msg
            if emailCode is None:
                return ok, '验证码不能为空'

            serverEmailCode = cache.get('syl_' + email, None)
            if serverEmailCode is None:
                return ok, '验证码已过期'
            cache.delete('syl_' + email)
            if serverEmailCode != emailCode:
                return ok, '验证码错误'
        except Exception as e:
            return False, 'Timeout'
        return True, None
    
    # 设置新密码
    def setNewPassword(self, email, newPwd):
        try:
            userObj = models.User.objects.get(email=email)
            userObj.pwd = genearteMD5(newPwd)
            userObj.save()
        except Exception as e:
            return False, '重置密码失败'
        return True, '重置密码成功'




