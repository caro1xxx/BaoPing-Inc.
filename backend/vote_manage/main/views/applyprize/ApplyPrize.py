from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
import json
from main.tools import myPaginator
from main.views.Common import Common


class ApplyPrize(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            # value = request.GET.get('value', None)

            # if value in ['all', None]:
            #     obj =  models.ApplyPrize.objects.all()
            # else:
            #     obj = models.ApplyPrize.objects.filter()

            # data, ret['page_count'] = myPaginator(obj, 10, request.GET.get('page_num', 1))
            # ret['data'] = serializers.serialize('json', data, use_natural_foreign_keys=True)
            ret['data'], ret['page_count'] = Common().getData(request, 'ApplyPrize', desc_order=True)

        except Exception as e:
            # ret = {'code': 500, 'msg':  'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
    

    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            pk = json.loads(request.body).get('pk', None)
            status = json.loads(request.body).get('status', None)

            if status is None:
                return JsonResponse({'code': 400, 'msg': 'status错误'})
            obj = models.ApplyPrize.objects.get(pk=pk)
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
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)