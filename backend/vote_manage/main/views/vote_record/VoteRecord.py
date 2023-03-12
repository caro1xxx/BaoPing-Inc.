from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
import json
from main.tools import *
from django.core.paginator import Paginator


class VoteRecord(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            value = request.GET.get('value', None)
            vote_id = request.GET.get('vote_id', None)

            if value in ['all', None, '']:
                voteRecordObj =  models.VoteRecord.objects.all() if vote_id is None else models.VoteRecord.objects.filter(vote_activity_id=vote_id)
            else:
                voteRecordObj = models.VoteRecord.objects.filter(voteuser__wx_username__contains=value) if vote_id is None else models.VoteRecord.objects.filter(voteuser__wx_username__contains=value, vote_activity_id=vote_id)

            data = voteRecordObj.order_by('-pk')
            # print(data[1])
            data, ret['page_count'] = myPaginator(data, 20, request.GET.get('page_num', 1))
            ret['data'] = serializers.serialize('json', data, use_natural_foreign_keys=False)

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
            voteRecordObj = models.VoteRecord.objects.filter(pk=pk).first()
            if not voteRecordObj:
                return JsonResponse({'code': 400, 'msg': '记录不存在'})         

            # 删除
            voteRecordObj.delete()
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
