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
                    officialcount_name = "",
                    app_id = "",
                    wxpay_pos_id = "",
                    wxpay_apiv2_secret_key = "",
                    wxpay_apiv3_secret_key = "",
                    wxpay_mchid = "",
                    wxpay_appid = "",
                    wxpay_app_key = "",
                    wxpay_notify_url = "",
                )
            accountObj = models.OfficialAccount.objects.get(pk=1)
            # ret['data'] = model_to_dict(accountObj)
            ret['data'] = serializers.serialize('json', [accountObj])
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
    
    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            data = json.loads(str(request.body, encoding='utf-8')).get('data', None)
            # data = json.loads(request.body).get('data', None)
            accountObj = models.OfficialAccount.objects.all().first()

            officialcount_name = data.get('officialcount_name', '')
            region = data.get('region', '')
            wxpay_pos_id = data.get('wxpay_pos_id', '')
            wxpay_apiv2_secret_key = data.get('wxpay_apiv2_secret_key', '')
            wxpay_apiv3_secret_key = data.get('wxpay_apiv3_secret_key', '')
            wxpay_mchid = data.get('wxpay_mchid', '')
            wxpay_appid = data.get('wxpay_appid', '')
            wxpay_app_key = data.get('wxpay_app_key', '')
            wxpay_notify_url = data.get('wxpay_notify_url', '')

            # validate = Validate()
            # validate.addCheck('checkIsNotEmpty', officialcount_name, '商户名不能为空')
            # validate.addCheck('checkIsNotEmpty', app_id, 'appid不能为空')
            # validate.addCheck('checkIsNotEmpty', region, 'region不能为空')
            # validate.addCheck('checkIsNotEmpty', wxpay_pos_id, '微信支付商户号不能为空')
            # validate.addCheck('checkIsNotEmpty', wxpay_apiv2_secret_key, '微信支付APIv2密钥不能为空')
            # validate.addCheck('checkIsNotEmpty', wxpay_apiv3_secret_key, '微信支付APIv3密钥不能为空')
            # ok, msg = validate.startCheck()
            # if not ok:
            #     return JsonResponse({'cod': 400, 'msg': msg})
            
            accountObj = models.OfficialAccount.objects.get(pk=1)
            accountObj.officialcount_name = officialcount_name
            accountObj.region = region
            accountObj.wxpay_pos_id = wxpay_pos_id
            accountObj.wxpay_apiv2_secret_key = wxpay_apiv2_secret_key
            accountObj.wxpay_apiv3_secret_key = wxpay_apiv3_secret_key
            accountObj.wxpay_mchid = wxpay_mchid
            accountObj.wxpay_appid = wxpay_appid
            accountObj.wxpay_app_key = wxpay_app_key
            accountObj.wxpay_notify_url = wxpay_notify_url
            accountObj.save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)