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

            if value in ['all', None, '']:
                voteRecordObj =  models.VoteRecord.objects.all()
            else:
                voteRecordObj = models.VoteRecord.objects.filter(voteuser__wx_username__contains=value)

            # data = []
            # for voteRecord in voteRecordObj:
            #     tmp = {}
            #     tmp['vote_user_wx_open_id'] = voteRecord.voteuser.open_id
            #     tmp['vote_user_wx_username'] = voteRecord.voteuser.wx_username
            #     tmp['vote_id'] = voteRecord.vote_activity.vote_id
            #     tmp['ip'] = voteRecord.ip
            #     tmp['phone_number'] = voteRecord.phone_number
            #     tmp['system'] = voteRecord.system
            #     tmp['network'] = voteRecord.network
            #     tmp['create_time'] = voteRecord.create_time
            #     data.append(tmp)

            data = voteRecordObj
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
            voteRecordId = json.loads(request.body).get('vote_record_id', None)
            
            # 验证参数
            validate = Validate()
            validate.addCheck('checkIsNotEmpty', voteRecordId, 'record_id不能为空')
            validate.addCheck('checkIsNumber', voteRecordId, 'record_id错误')
            ok, msg = validate.startCheck()
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            voteRecordObj = models.VoteRecord.objects.filter(pk=voteRecordId).first()
            if not voteRecordObj:
                return JsonResponse({'code': 400, 'msg': '记录不存在'})         

            # 删除
            voteRecordObj.delete()
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
