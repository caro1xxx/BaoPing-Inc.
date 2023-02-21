import json
from main import models
from main.models import domain
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers


# get获取一个可用域名，post包含add和update方法
class GetDomain(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            # ret['domainlist'] = serializers.serialize("json", domain.objects.filter(status=1))
            ret['domain'] = models.domain.objects.filter(status=1).first().domain
            return JsonResponse(ret)
        except Exception as e:
            ret['code'] = 500
            ret['msg'] = 'Timeout'
        return JsonResponse(ret)


    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            fun = json.loads(request.body).get('fun', None)
            domainz = json.loads(request.body).get('domain', None)
            status = json.loads(request.body).get('status', None)
            if not domainz:
                ret['code'] = 404
                ret['msg'] = 'domain does not exist'
                return JsonResponse(ret)
            if fun == 'add':
                if not status:
                    ret['code'] = 400
                    ret['msg'] = 'status error'
                    return JsonResponse(ret)
                domains = models.domain.objects.filter(domain=str(domainz))
                if domains.exists():
                    ret['code'] = 400
                    ret['msg'] = 'domain already exist'
                    return JsonResponse(ret)
                domain_obj = models.domain.objects.create(domain=str(domainz), status=int(status))
                domain_obj.save()
            elif fun == 'update':
                domain_obj = domain.objects.get(domain=str(domainz))
                domain_obj.status = 0 if domain_obj.status else 1
                domain_obj.save()
            else:
                ret['code'] = 404
                ret['msg'] = 'fun error'
                return JsonResponse(ret)
            return JsonResponse(ret)
        except Exception as e:
            ret['code'] = 500
            ret['msg'] = 'Timeout'
            ret['error'] = str(e)
        return JsonResponse(ret)

# post包含add和update功能
class Active(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            domainList = json.loads(request.body).get('domain_list')
            fun = json.loads(request.body).get('fun')
            domainList = [] if not domainList else serializers.serialize("json", domainList)
            if fun == 'add':
                activeObj = models.Active.objects.create(domain_list=domainList)
                activeObj.save()
            elif fun == 'update':
                idx = json.loads(request.body).get('id')
                if not idx:
                    ret['code'] = 400
                    ret['msg'] = 'Parameter error'
                    return JsonResponse(ret)
                activeObj = models.Active.objects.get(id=int(idx))
                activeObj.domain_list = domainList
                activeObj.save()
            else:
                ret = {'code': 404, 'msg': 'fun error'}
        except Exception as e:
            ret['code'] = 500
            ret['msg'] = 'Timeout'
            ret['error'] = str(e)
        return JsonResponse(ret)
