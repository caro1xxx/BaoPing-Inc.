from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
import json
from main.tools import *
from main.views.Common import Common


class Domain(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            # value = request.GET.get('value', None)

            # if value in ['all', None]:
            #     domainObj =  models.Domain.objects.all()
            # else:
            #     domainObj = models.Domain.objects.filter()
            
            # data = domainObj
            # data, ret['page_count'] = myPaginator(data, 10, request.GET.get('page_num', 1))
            # ret['data'] = serializers.serialize('json', data, use_natural_foreign_keys=True)
            ret['data'], ret['page_count'] = Common().getData(request, 'Domain', maxsize=20)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '创建成功'}
        try:
            # 接收参数
            domain = json.loads(request.body).get('domain', None)
            expireTime = json.loads(request.body).get('expire_time', None)

            # 验证数据
            validate = Validate()
            validate.addCheck('checkIsNotEmpty', domain, '域名不能为空')
            validate.addCheck('checkIsNotEmpty', domain, '域名不能为空')
            # validate.addCheck('checkIsDomain', domain, '域名格式错误')
            validate.addCheck('checkIsNotEmpty', expireTime, '过期时间不能为空')
            validate.addCheck('checkIsNumber', expireTime, '过期时间格式错误')
            ok, msg = validate.startCheck()
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            if models.Domain.objects.filter(domain_name=domain).first():
                return JsonResponse({'code': 400, 'msg': '域名重复'})

            # 创建
            models.Domain.objects.create(
                domain_name = domain,
                status = 1,
                visit_count = 0,
                expire_time = expireTime,
                flow = 0,
                vote_id = 0
            ).save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            # 接收参数
            domainName = json.loads(request.body).get('domain', None)
            key = json.loads(request.body).get('key', None)
            value = json.loads(request.body).get('value', None)
            
            # 验证数据
            validate = Validate()
            validate.addCheck('checkIsNotEmpty', domainName, '域名不能为空')
            validate.addCheck('checkIsDomain', domainName, '域名错误')
            ok, msg = validate.startCheck()
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            domainObj = models.Domain.objects.filter(domain_name=domainName).first()
            if not domainObj:
                return JsonResponse({'code': 400, 'msg': '记录不存在'})
                
            # 进行修改
            if key == 'expire_time':
                validate.addCheck('checkIsNotEmpty', value, '过期时间不能为空')
                validate.addCheck('checkIsNumber', value, '过期时间错误')
                ok, msg = validate.startCheck()
                if not ok:
                    return JsonResponse({'code': 400, 'msg': msg})
                
                domainObj.expire_time = value
            elif key == 'status':
                validate.addCheck('checkIsNotEmpty', value, '状态不能为空')
                validate.addCheck('checkIsNumber', value, '状态错误')
                ok, msg = validate.startCheck()
                if not ok:
                    return JsonResponse({'code': 400, 'msg': msg})
                
                domainObj.status = value
            else:
                return JsonResponse({'code': 400, 'msg': '参数错误'})
            
            domainObj.save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '删除成功'}
        try:
            # 接收数据
            domainName = json.loads(request.body).get('domain', None)
            
            # 验证参数
            validate = Validate()
            validate.addCheck('checkIsNotEmpty', domainName, '域名ID不能为空')
            ok, msg = validate.startCheck()
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            domainObj = models.Domain.objects.filter(domain_name=domainName).first()
            if not domainObj:
                return JsonResponse({'code': 400, 'msg': '记录不存在'})         

            # 删除
            domainObj.delete()
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
