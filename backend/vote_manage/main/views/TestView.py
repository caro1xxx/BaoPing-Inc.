from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import generateCode6
import json
from main.tools import Validate
from main.views.vote_activity.VoteActivityOp import VoteActivityOp
from django.core.paginator import Paginator
from vote_manage.settings import BASE_DIR
import geoip2.database
from vote_manage import settings


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        ret = {}
            
        reader = geoip2.database.Reader(str(settings.STATIC_ROOT) + '/GeoLite2-City_20230307/' + 'GeoLite2-City.mmdb')
        ip = request.GET.get('ip', None)
        response = reader.city(ip)
        # ret['region'] = "地区：{}({})".format(response.continent.names["es"], response.continent.names["zh-CN"])
        # ret['country'] = "国家：{}({}) ，简称:{}".format(response.country.name, response.country.names["zh-CN"], response.country.iso_code)
        # ret['city'] = "城市：{}({})".format(response.city.name, response.city.names["zh-CN"])
        # ret['rgion'] = str(response.continent)
        ret['city'] = str(response.country.name)
        ret['city'] = str(response.city.name)
        return JsonResponse(ret)
    
    def post(self, request, *args, **kwargs):
        print('test')
        return JsonResponse({})
        try:
            file_obj = request.FILES.get('file')
            import os
            f = open(os.path.join(BASE_DIR, 'static', 'pic', file_obj.name), 'wb')
            print(file_obj,type(file_obj))
            for chunk in file_obj.chunks():
                f.write(chunk)
            f.close()
            print('11111')
            return JsonResponse({})
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'msg': str(e)}
            return JsonResponse(ret)