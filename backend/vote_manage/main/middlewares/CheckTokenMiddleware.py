from django.utils.deprecation import MiddlewareMixin
from main.views.user.UserOp import UserOp
import json
from main import models
from main.views.user.UserOp import UserOp
from main.tools import *
from django.http import JsonResponse



class CheckTokenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            print('checktokenmiddleware test')
            m = str(request.method)
            if m == 'GET':
                token = request.GET.get('token', None)
            elif m in ['POST', 'PUT', 'DELETE']:
                token = json.loads(request.body).get("token", None)
            else:
                return JsonResponse({"code": 400, "msg": "身份验证失败"})
            
            userop = UserOp() 
            if token:
                username, lastLoginTime = userop.getDataFromToken(token)
                print(username, lastLoginTime)
                userObj = models.User.objects.get(username=username)
                serverUsername, serverLastLoginTime = userop.getDataFromToken(userObj.token)
                if token == userObj.token and getNowTimeStamp() - lastLoginTime > 7 * 24 * 60:
                    return JsonResponse({"code": 400, "msg": "登陆超时"})
        except Exception as e:
            return JsonResponse({"code": 400, "msg": "身份验证失败"})
            # return JsonResponse({"code": 400, "msg": "身份验证失败", "error": str(e)})
        # print("middleware test")
        # userop = UserOp() 
        # token = json.loads(request.body).get('token', None)

        # if token:
        #     username, lastLoginTime = userop.getDataFromToken(token)
        #     userObj = models.User.objects.get(username=username)
        #     serverUsername, serverLastLoginTime = userop.getDataFromToken(userObj.token)
        #     if token == userObj.token:
        #         if getNowTimeStamp() - lastLoginTime > 7 * 24 * 60 * 60:
        #             return JsonResponse({"code": 400, "msg": "登陆超时"})
        #     else:
        #         return JsonResponse({"code": 400, "msg": "身份验证失败"})
