from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
import json
from main.tools import *
from main.views.Common import Common


class QueryPaymentStatus(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            payment_order_id = request.GET.get('order_id', None)

            if payment_order_id is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})

            paymentRecordObj = models.PaymentRecord.objects.filter(payment_order_id=payment_order_id).first()
            if paymentRecordObj is None:
                return JsonResponse({'code': 400, 'msg': '该订单不存在'})
            
            # ret['status'] = 
            ret['code'] = 400 if paymentRecordObj.payment_status != 1 else ret['code']
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)