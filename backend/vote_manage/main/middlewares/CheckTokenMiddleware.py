from django.utils.deprecation import MiddlewareMixin
from main.views.user.UserOp import UserOp
import json
from main import models
from main.views.user.UserOp import UserOp
from main.tools import *
from django.http import JsonResponse
from main.models import Token

class CheckTokenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            # print('checktokenmiddleware test')
            m = str(request.method)
            pathInfo = request.path_info.replace('/', '').replace('api', '')
            if pathInfo in [
                'login', 
                'register', 
                'forgetpasswordsendemail', 
                'sendemailcode', 
                'statics', 
                'staticshistory', 
                'uploadfile',
                'querypayment',
                'paymentrecord',
                'queryquerypaymentstatus',
                ] or str(pathInfo).find('media') != -1:
                return None
            if m == 'GET':
                if pathInfo in ['settings', 'alonevoteactivity', 'votetarget']:
                    return None
                token = request.GET.get('token', None)
            elif m in ['POST', 'PUT', 'DELETE']:
                # print(str(request.body, encoding='utf-8'))
                if pathInfo in ['setnewpassword']:
                    return None

                if request.FILES:
                    token = request.POST.get('token', None)
                else:
                    token = json.loads(request.body).get("token", None)
                # token = json.loads(str(request.body, encoding='utf-8')).get("token", None)
            else:
                return JsonResponse({"code": 400, "msg": "身份验证失败"})
            userop = UserOp() 

            if token:
                tokenModel = models.Token.objects.filter(value=token).first()
                if not tokenModel:
                    return JsonResponse({"code": 404, "msg": "token不存在"})
                if tokenModel.expire_time < getNowTimeStamp():
                    return JsonResponse({"code": 405, "msg": "token过期"})
            else:
                return JsonResponse({"code": 400, "msg": "缺失token"})

                
        except Exception as e:
            # return JsonResponse({"code": 500, "msg": "身份验证失败"})
            return JsonResponse({"code": 500, "msg": "身份验证失败", "error": str(e)})
