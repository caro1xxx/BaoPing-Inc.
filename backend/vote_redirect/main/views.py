import json
from main import models
from main.models import domain
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.DomainOp import DomainOp


# get获取一个可用域名，post包含add和update方法
class GetDomain(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            voteId = request.GET.get('vote_id', None)
            if voteId is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})
            
            domainObj = models.domain.objects.filter(status=1, vote_id=voteId).all().order_by('visit_count').first()
            if domainObj is None:
                return JsonResponse({'code': 400, 'msg': 'not found'})
            
            DomainOp().addVisitCount(domainObj)
            ret['domain'] = domainObj.domain_name

        except Exception as e:
            return JsonResponse({'code': 500, 'msg': 'Timeout'})
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
            return JsonResponse({'code': 500, 'msg': 'Timeout'})
        return JsonResponse(ret)

# get查询某域名的访问量，post将某域名的访问量+1
class DomainVisCnt(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            domain_name = request.GET.get('domain', None)
            if domain_name is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})
            
            domainObj = models.domain.objects.filter(domain_name=domain_name).first()
            if domainObj is None:
                return JsonResponse({'code': 400, 'msg': 'not found'})
            
            ret['visit_count'] = domainObj.visit_count

        except Exception as e:
            return JsonResponse({'code': 500, 'msg': 'Timeout'})
        return JsonResponse(ret)

    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            domain_name = json.loads(request.body).get('domain', None)
            if domain_name is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})
            
            domainObj = models.domain.objects.filter(domain_name=domain_name).first()
            if domainObj is None:
                return JsonResponse({'code': 400, 'msg': 'not found'})
            
            DomainOp().addVisitCount(domainObj)

        except Exception as e:
            return JsonResponse({'code': 500, 'msg': 'Timeout'})
        return JsonResponse(ret)
 


# 用于编写代码时test
class TestFun(APIView):
    def get(self, request, *args, **kwargs):
        pass

