import json
from main import models
from django.http import JsonResponse
from rest_framework.views import APIView
from main.tools import getNowTimeStamp
from main.views.wxpay import wxpay_tools


class UserInfo(APIView):
    # 获取全部用户信息
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            code = request.GET.get('code', None)
            
            ok, accessToken = wxpay_tools.getAccessToken()
            if not ok:
                return JsonResponse({'code': 400, 'msg': accessToken})

            ok, openid = wxpay_tools.getOpenid(code)
            if not ok:
                return JsonResponse({'code': 400, 'msg': openid})

            ret['openid'] = openid


        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)