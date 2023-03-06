from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import generateCode6, myPaginator
import json
from main.tools import Validate
from main.views.vote_activity.VoteActivityOp import VoteActivityOp
from main.views.Common import Common


class VoteActivity(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            # value = request.GET.get('value', None)

            # if not value:
            #     obj =  models.VoteActivity.objects.all()
            # else:
            #     obj = models.VoteActivity.objects.filter(domain__contains=value)

            # data, ret['page_count'] = myPaginator(obj, 10, request.GET.get('page_num', 1))
            # ret['data'] = serializers.serialize('json', data, use_natural_foreign_keys=True)
            ret['data'], ret['page_count'] = Common().getData(request, 'VoteActivity')

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'msg': str(e)}
        return JsonResponse(ret)

    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '创建成功'}
        try:
            # data = json.loads(request.body).get('data', None)
            data ={}
            data['vote_name'] = request.POST.get('vote_name', None)
            data['create_user_username'] = request.POST.get('create_user_username', None)
            data['create_time'] = request.POST.get('create_time', None)
            data['expire_time'] = request.POST.get('expire_time', None)
            data['img'] = request.FILES.get('img', None)

            validate = Validate()
            validate.addCheck('checkIsNotEmpty', data['vote_name'], '活动名称不能为空')
            validate.addCheck('checkIsNotEmpty', data['create_user_username'], '创建者不能为空')
            validate.addCheck('checkIsNotEmpty', data['create_time'], '活动开始时间不能为空')
            # validate.addCheck('checkIsNotEmpty', data['img'], '缩略图不能为空')
            validate.addCheck('checkIsNotEmpty', data['expire_time'], '活动结束时间不能为空')
            validate.addCheck('checkIsNumber', data['create_time'], '活动开始时间错误')
            validate.addCheck('checkIsNumber', data['expire_time'], '活动结束时间错误')
            ok, msg = validate.startCheck()
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            if not models.User.objects.filter(username=data['create_user_username']).first():
                return JsonResponse({'code': 400, 'msg': '创建者错误'})
            domainObj = models.Domain.objects.filter(status=1).order_by('visit_count').first()
            domain_name = '' if domainObj is None else domainObj.domain_name
            if not domain_name:
                return JsonResponse({'code': 400, 'msg': '暂时没有可用域名，无法创建活动'})

            models.VoteActivity.objects.create(
                name = data['vote_name'],
                create_user_id = data['create_user_username'],
                img = data['img'],
                domain_id = domain_name,
                vote_id = generateCode6(),
                create_time = data['create_time'],
                expire_time = data['expire_time'],
            ).save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout',   'error': str(e)}
        return JsonResponse(ret)

    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            data = json.loads(request.body).get('data', None)

            if data is None:
                return JsonResponse({'code': 400, 'msg': '数据错误'})
            content = data.get('content', None)
            if content is None:
                return JsonResponse({'code': 400, 'msg': '参数错误'})
                
            voteActivityOp = VoteActivityOp()
            if content == 'activity_settings':
                ok, msg = voteActivityOp.checkActivityData(data)
                if not ok:
                    return JsonResponse({'code': 400, 'msg': msg})
                voteActivityOp.updateActivityData(data)
                
            elif content == 'vote_settings':
                ok, msg = voteActivityOp.checkVoteData(data)
                if not ok:
                    return JsonResponse({'code': 400, 'msg': msg})
                voteActivityOp.updateVoteData(data)

            elif content == 'auto_comment_settings':
                ok, msg = voteActivityOp.checkAutoCommentData(data)
                if not ok:
                    return JsonResponse({'code': 400, 'msg': msg})
                voteActivityOp.updateAutoCommentData(data)

            elif content == 'template':
                ok, msg = voteActivityOp.checkTemplateData(data)
                if not ok:
                    return JsonResponse({'code': 400, 'msg': msg})
                voteActivityOp.updateTemplateData(data)
            else:
                return JsonResponse({'code': 400, 'msg': '参数错误'})
            
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '删除成功'}
        try:
            voteId = json.loads(request.body).get('vote_id', None)
             
            feedbackObj = models.VoteActivity.objects.filter(vote_id=voteId).first()
            if not feedbackObj:
                return JsonResponse({'code': 400, 'msg': 'ID错误'})
            feedbackObj.delete()
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)