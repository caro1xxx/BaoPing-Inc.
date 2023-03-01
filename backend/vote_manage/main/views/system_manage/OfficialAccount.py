import json
from main import models
from django.forms.models import model_to_dict
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.tools import Validate
from main.views.user.UserOp import UserOp


class OfficialAccount(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            accountObj = models.OfficialAccount.objects.all().first()
            if accountObj is None:
                models.OfficialAccount.objects.create(
                    name = "",
                    app_id = "",
                    region = "",
                    wx_pay_pos_id = "",
                    wx_pay_apiv2_secret_key = "",
                    wx_pay_apiv3_secret_key = "",
                ).save()
            accountObj = models.OfficialAccount.objects.get(pk=1)
            ret['data'] = model_to_dict(accountObj)
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
    
    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            data = json.loads(str(request.body, encoding='utf-8')).get('data', None)
            # data = json.loads(request.body).get('data', None)
            accountObj = models.OfficialAccount.objects.all().first()

            name = data.get('name', None)
            app_id = data.get('app_id', None)
            region = data.get('region', None)
            wx_pay_pos_id = data.get('wx_pay_pos_id', None)
            wx_pay_apiv2_secret_key = data.get('wx_pay_apiv2_secret_key', None)
            wx_pay_apiv3_secret_key = data.get('wx_pay_apiv3_secret_key', None)

            validate = Validate()
            validate.addCheck('checkIsNotEmpty', name, '商户名不能为空')
            validate.addCheck('checkIsNotEmpty', app_id, 'appid不能为空')
            validate.addCheck('checkIsNotEmpty', region, 'region不能为空')
            validate.addCheck('checkIsNotEmpty', wx_pay_pos_id, '微信支付商户号不能为空')
            validate.addCheck('checkIsNotEmpty', wx_pay_apiv2_secret_key, '微信支付APIv2密钥不能为空')
            validate.addCheck('checkIsNotEmpty', wx_pay_apiv3_secret_key, '微信支付APIv3密钥不能为空')
            ok, msg = validate.startCheck()

            if not ok:
                return JsonResponse({'cod': 400, 'msg': msg})
            
            accountObj = models.OfficialAccount.objects.get(pk=1)
            accountObj.name = name
            accountObj.app_id = app_id
            accountObj.region = region
            accountObj.wx_pay_pos_id = wx_pay_pos_id
            accountObj.wx_pay_apiv2_secret_key = wx_pay_apiv2_secret_key
            accountObj.wx_pay_apiv3_secret_key = wx_pay_apiv3_secret_key
            accountObj.save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)