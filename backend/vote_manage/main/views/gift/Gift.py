from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
import json
from main.views.Common import Common
from main.views.gift.GiftOp import GiftOp
from main import models


class Gift(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            ret['data'], ret['page_count'] = Common().getData(request, 'Gift')

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
    
    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '添加成功'}
        try:
            data = json.loads(request.body).get('data', None)

            if data is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})
            
            giftOp = GiftOp()
            ok, msg = giftOp.checkDataOnCreate(data)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            
            giftOp.create(data)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
    
    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            data = json.loads(request.body).get('data', None)

            if data is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})
            
            giftOp = GiftOp()
            ok, msg = giftOp.checkDataOnUpdate(data)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            print(1)
            giftOp.update(data)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
    
    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '删除成功'}
        try:
            pk = json.loads(request.body).get('pk', None)

            if pk in [None, '']:
                return JsonResponse({'code': 400, 'msg': '参数错误'})
            giftOp = GiftOp()
            ok, msg = giftOp.checkGiftIsExist(pk)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            
            models.Gift.objects.filter(pk=pk).first().delete()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
    