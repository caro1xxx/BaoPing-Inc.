from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
import json
from main.tools import myPaginator


class ApplyPrize(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            value = request.GET.get('value', None)

            if value in ['all', None]:
                obj =  models.ApplyPrize.objects.all()
            else:
                obj = models.ApplyPrize.objects.filter()
            # data = []
            # for applyPrize in obj:
            #     tmp = {}
            #     tmp['apply_prize_id'] = applyPrize.pk
            #     tmp['username'] = applyPrize.voteuser.wx_username
            #     tmp['name'] = applyPrize.name
            #     tmp['phone_number'] = applyPrize.phone_number
            #     tmp['create_time'] = applyPrize.create_time
            #     tmp['status'] = applyPrize.status
            #     data.append(tmp)

            data, ret['page_count'] = myPaginator(obj, 10, request.GET.get('page_num', 1))
            ret['data'] = serializers.serialize('json', data, use_natural_foreign_keys=True)

        except Exception as e:
            # ret = {'code': 500, 'msg':  'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'msg': str(e)}
        return JsonResponse(ret)
    

    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            applyPrizeId = json.loads(request.body).get('apply_prize_id', None)
            status = json.loads(request.body).get('status', None)

            if status is None:
                return JsonResponse({'code': 400, 'msg': 'status错误'})
            obj = models.ApplyPrize.objects.get(pk=applyPrizeId)
            if not obj:
                return JsonResponse({'code': 400, 'msg': 'ID错误'})
                
            obj.status = status
            obj.save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'msg': str(e)}
        return JsonResponse(ret)

    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '删除成功'}
        try:
            pk = json.loads(request.body).get('pk', None)
            feedbackObj = models.ApplyPrize.objects.get(pk=int(pk))
            if not feedbackObj:
                return JsonResponse({'code': 400, 'msg': 'ID错误'})
            feedbackObj.delete()
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)