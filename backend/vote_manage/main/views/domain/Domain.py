from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
import json


class Domain(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            value = request.GET.get('value', None)

            if value in ['all', None]:
                domainObj =  models.Domain.objects.all()
            else:
                domainObj = models.Domain.objects.filter()

            ret['data'] = serializers.serialize('json', domainObj)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '创建成功'}
        try:
            domain = json.loads(request.body).get('domain', None)
            expireTime = json.loads(request.body).get('expire_time', None)

            # validate data

            models.Domain.objects.create(
                domain = domain,
                status = 1,
                vis_cnt = 0,
                expire_time = expireTime,
                flow = 0
            ).save()

        except Exception as e:
            # ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
        pass

    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            domainId = json.loads(request.body).get('domain_id', None)
            key = json.loads(request.body).get('key', None)
            value = json.loads(request.body).get('value', None)

            domainObj = models.Domain.objects.get(pk=domainId)
            if key == 'expire_time':
                domainObj.expire_time = value
            elif key == 'status':
                domainObj.status = value
            else:
                return JsonResponse({'code': 400, 'msg': '参数错误'})
            domainObj.save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '删除成功'}
        try:
            domainId = json.loads(request.body).get('domain_id', None)
             
            domainObj = models.Domain.objects.get(pk=domainId)
            if not domainObj:
                return JsonResponse({'code': 400, 'msg': 'ID错误'})
            domainObj.delete()
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
        return JsonResponse(ret)
