import json
from main import models
from main.models import domain
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers


# Create your views here.
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
            return JsonResponse(ret)
        except Exception as e:
            ret['code'] = 500
            ret['msg'] = 'Timeout'
            ret['error'] = str(e)
        return JsonResponse(ret)
