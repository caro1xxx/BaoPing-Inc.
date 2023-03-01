from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
import json
from main.tools import *


class PaymentRecord(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            value = request.GET.get('value', None)

            if value in ['all', None, '']:
                paymentRecordObj =  models.PaymentRecord.objects.all()
            else:
                paymentRecordObj = models.PaymentRecord.objects.filter()

            # data = []
            # for paymentRecord in paymentRecordObj:
            #     tmp = {}
            #     tmp['vote_user_wx_open_id'] = paymentRecord.voteuser.open_id
            #     tmp['vote_user_wx_username'] = paymentRecord.voteuser.wx_username
            #     tmp['vote_id'] = paymentRecord.vote_activity.vote_id
            #     tmp['price'] = paymentRecord.price
            #     tmp['prize_type'] = paymentRecord.prize_type
            #     tmp['payment_order_id'] = paymentRecord.payment_order_id
            #     tmp['payment_status'] = paymentRecord.payment_status
            #     tmp['ip'] = paymentRecord.ip
            #     tmp['phone_number'] = paymentRecord.phone_number
            #     tmp['system'] = paymentRecord.system
            #     tmp['network'] = paymentRecord.network
            #     tmp['create_time'] = paymentRecord.create_time
            #     data.append(tmp)
            data = paymentRecordObj
            data, ret['page_count'] = myPaginator(data, 10, request.GET.get('page_num', 1))
            ret['data'] = serializers.serialize('json', data, use_natural_foreign_keys=True)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '删除成功'}
        try:
            # 接收数据
            paymentRecordId = json.loads(request.body).get('payment_record_id', None)
            
            # 验证参数
            validate = Validate()
            validate.addCheck('checkIsNotEmpty', paymentRecordId, 'record_id不能为空')
            validate.addCheck('checkIsNumber', paymentRecordId, 'record_id错误')
            ok, msg = validate.startCheck()
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            voteRecordObj = models.PaymentRecord.objects.filter(pk=paymentRecordId).first()
            if not voteRecordObj:
                return JsonResponse({'code': 400, 'msg': '记录不存在'})         

            # 删除
            voteRecordObj.delete()
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
