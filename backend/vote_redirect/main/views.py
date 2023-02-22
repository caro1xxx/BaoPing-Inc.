import json
from main import models
from main.models import domain
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache


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

# post实现两个功能，传入add将访问次数加1，传入query查询域名访问次数
class DomainVisCnt(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        # domainList = json.loads(request.body).get('fun')
        try:
            fun = json.loads(request.body).get('fun')
            domainName = json.loads(request.body).get('domain')
            if not domainName:
                ret = {'code': 404, 'msg': 'domain does not exist'}
                return JsonResponse(ret)
            if fun == 'query':
                res = self.queryCnt(domainName)
                if res:
                    ret['vis_cnt'] = res
                else:
                    ret['code'] = 404
                    ret['msg'] = 'failed'
                    return ret
            elif fun == 'add':
                ok = self.addCnt(domainName)
                if not ok:
                    ret['code'] = 404
                    ret['msg'] = 'add visit failed'
                    return ret
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            return ret
        return JsonResponse(ret)

    # 查询域名访问数量
    def queryCnt(self, domainName):
        cnt = 0
        try:
            if cache.get(domainName, None):
                cnt = cache.get(domainName, None)
            else:
                domainObj = models.domain.objects.filter(domain=str(domainName))
                if domainObj.exists():
                    cnt = domainObj.first().vis_cnt
                else:
                    return False
                cache.set(domainName, cnt)
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            return ret
        return cnt

    # 将一个域名访问数量+1
    def addCnt(self, domainName):
        try:
            cnt = cache.get(domain, None)
            if cnt:
                cnt = int(cnt) + 1
                cache.set(domain, cnt)
                domainObj = models.domain.objects.get(domain=str(domainName))
                domainObj.vis_cnt = cnt
                domainObj.save()
            else:
                domainObj = models.domain.objects.filter(domain=str(domainName))
                if domainObj.exists():
                    domainObj = models.domain.objects.get(domain=str(domainName))
                    domainObj.vis_cnt = domainObj.vis_cnt + 1
                    cache.set(domainName, domainObj.vis_cnt)
                    domainObj.save()
                else:
                    return False
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            return ret
        return True

# 用于编写代码时test
class TestFun(APIView):
    def get(self, request, *args, **kwargs):
        pass


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
