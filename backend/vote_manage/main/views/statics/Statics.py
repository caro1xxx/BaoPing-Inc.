from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import *
from main.views.statics.StaticsOp import StaticsOp


class Statics(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            staticsObj = models.Statics.objects.all()
            data = serializers.serialize('json', staticsObj)
            # return JsonResponse(ret)

            staticsOp = StaticsOp()
            if staticsObj is None:
                staticsObj = staticsOp.initStatics()
                ret['data'] = staticsObj 
                return JsonResponse(ret)
            else:
                staticsObj = staticsOp.updateStatics()
                ret['data'] = staticsObj 
                return JsonResponse(ret)          

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)