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


