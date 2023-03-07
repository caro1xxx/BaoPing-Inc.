from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
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
                ret['data'], ret['page_count'] = Common().getData(request, 'PaymentRecord')
            else:
                data = models.PaymentRecord.objects.filter(vote_activity_id=vote_id)
                data, ret['page_count'] = myPaginator(data, 10, request.GET.get('page_num', 1))
                ret['data'] = serializers.serialize('json', data, use_natural_foreign_keys=True)

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
