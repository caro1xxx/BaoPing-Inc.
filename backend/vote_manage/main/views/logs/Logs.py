import json
from main import models
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from main.views.user.UserOp import UserOp
from main.tools import Validate, getNowTimeStamp, myPaginator

class Logs(APIView): 
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            value = request.GET.get('value', None)

            if value in ['all', None, '']:
                logsObj =  models.Logs.objects.all()
            else:
                logsObj = models.Logs.objects.filter(action=value)

            data = logsObj
            data, ret['page_count'] = myPaginator(data, 10, request.GET.get('page_num', 1))
            ret['data'] = serializers.serialize('json', data, use_natural_foreign_keys=True)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
        return JsonResponse(ret)
    
    def post(self, request, *ary, **kwargs):
        ret = {'code': 200, 'msg': '添加日志成功'}
        try:
            who = json.loads(request.body).get('who', None)
            action = json.loads(request.body).get('action', None)
            target = json.loads(request.body).get('target', None)
            create_time = getNowTimeStamp()

            ck = Validate()
            ck.addCheck('checkIsNotEmpty', action, '行为不能为空')
            ck.addCheck('checkIsNotEmpty', target, '对象不能为空')
            ok, msg = ck.startCheck()
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})

            logsObj = models.Logs.objects.create(who=who, action=action, target=target, create_time=create_time)
            logsObj.save()
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)