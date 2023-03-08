import json
from main import models
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from main.views.user.UserOp import UserOp


class SetNewPassword(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 200, "msg": '重置密码成功'}
        try:
            email = json.loads(request.body).get('email', None) 
            emailCode = json.loads(request.body).get('code', None) 
            newPwd = json.loads(request.body).get('new_pwd', None) 

            userop = UserOp()
            ok, msg = userop.checkEmail(email)
            if not ok:
                return JsonResponse({'code': 400, "msg": msg})
            ok, msg = userop.checkEmailExist(email)
            if not ok:
                return JsonResponse({'code': 400, "msg": '邮箱未注册'})
            ok, msg = userop.checkEmailCode(email, emailCode)
            if not ok:
                return JsonResponse({'code': 400, "msg": msg})
            ok, msg = userop.checkPwd(newPwd)
            if not ok:
                return JsonResponse({'code': 400, "msg": msg})
            ok, msg = userop.setNewPassword(email, newPwd)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})

            userObj = models.User.objects.filter(email=email).first()
            userop.onLoginSuccess(userObj)
            ret['data'] = serializers.serialize("json", [userObj])
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)