from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from django.db.models import F
from main import models
import json
from main.tools import *
from main.views.Common import Common


class PaymentRecord(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            vote_id = request.GET.get('vote_id', None)

            if vote_id in [None, '']:
                ret['data'], ret['page_count'] = Common().getData(request, 'PaymentRecord', desc_order=True)
            else:
                data = models.PaymentRecord.objects.filter(vote_activity_id=vote_id)
                data, ret['page_count'] = myPaginator(data.order_by('-pk'), 10, request.GET.get('page_num', 1))
                ret['data'] = serializers.serialize('json', data, use_natural_foreign_keys=True)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            data = json.loads(request.body).get('data', None)

            # validate data
            orderId = generateString16()
            while True:
                if models.PaymentRecord.objects.filter(payment_order_id=orderId).first() is None:
                    break
                orderId = generateString16()
            support = models.Gift.objects.filter(name=data['body']).first().value
            
            models.PaymentRecord.objects.create(
                voteuser_id = data['openid'],
                vote_activity_id = data['vote_id'],
                price = data['total_fee'] / 100,
                create_time = getNowTimeStamp(),
                ip = getIp(request),
                phone_model = data['phone_model'],
                system = data['system'],
                network = data['network'],
                prize_type = data['body'],
                payment_order_id = orderId,
                payment_status = 0,
                support_count = support,
                vote_target = data['vote_target_id'],
                update_time = getNowTimeStamp(),
            )

            models.VoteTarget.objects.filter(pk=data['vote_target_id']).update(count = F('count') + support)
            ret['order_id'] = orderId

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            data = json.loads(request.body).get('data', None)
            payment_order_id = data.get('order_id', None)

            if payment_order_id is None:
                return JsonResponse({'code': 400, 'msg': '该订单不存在'})
            
            paymentRecordObj = models.PaymentRecord.objects.filter(payment_order_id=payment_order_id).first()
            if paymentRecordObj is None:
                return JsonResponse({'code': 400, 'msg': '该订单不存在'})

            paymentRecordObj.payment_status = data.get('status', 0)
            paymentRecordObj.update_time = getNowTimeStamp()
            paymentRecordObj.save()

            if data.get('status', 0) in ['1', 1]:
                models.VoteRecord.objects.create(
                    voteuser_id = paymentRecordObj.voteuser_id,
                    vote_target_id = paymentRecordObj.vote_target,
                    create_time = getNowTimeStamp(),
                    vote_activity = paymentRecordObj.vote_activity_id,
                    ip = paymentRecordObj.ip,
                    phone_model = paymentRecordObj.phone_model,
                    system = paymentRecordObj.system,
                    network = paymentRecordObj.network,
                    count = paymentRecordObj.support_count
                )

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '删除成功'}
        try:
            # 接收数据
            pk = json.loads(request.body).get('pk', None)
            
            # 验证参数
            validate = Validate()
            validate.addCheck('checkIsNotEmpty', pk, 'pk不能为空')
            validate.addCheck('checkIsNumber', pk, 'pk错误')
            ok, msg = validate.startCheck()
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            voteRecordObj = models.PaymentRecord.objects.filter(pk=pk).first()
            if not voteRecordObj:
                return JsonResponse({'code': 400, 'msg': '记录不存在'})         

            # 删除
            voteRecordObj.delete()
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)


