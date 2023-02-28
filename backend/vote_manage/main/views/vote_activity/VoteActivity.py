from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import generateString16
import json


class VoteActivity(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            value = request.GET.get('value', None)

            if value in ['all', None]:
                obj =  models.VoteActivity.objects.all()
            else:
                obj = models.VoteActivity.objects.filter(domain__contains=value)

            data = []
            for voteActivity in obj:
                tmp = {}
                tmp['name'] = voteActivity.create_user.name
                tmp['username'] = voteActivity.create_user.username
                tmp['domain'] = voteActivity.domain.domain
                tmp['flow'] = voteActivity.flow
                tmp['share'] = voteActivity.share
                tmp['img'] = voteActivity.img
                tmp['income'] = voteActivity.income
                tmp['params'] = voteActivity.params
                tmp['create_time'] = voteActivity.create_time
                tmp['expire_time'] = voteActivity.expire_time
                data.append(tmp)
            ret['data'] = data

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'msg': str(e)}
        return JsonResponse(ret)

    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '创建成功'}
        try:
            data = json.loads(request.body).get('data', None)

            # validate data

            domainObj = models.Domain.objects.filter(status=1).order_by('-vis_cnt').first()
            domain_id = '' if domainObj is None else domainObj.pk
            models.VoteActivity.objects.create(
                create_user_id = data['create_user_username'],
                img = data['img'],
                domain_id = domain_id,
                params = generateString16(),
                create_time = data['create_time'],
                expire_time = data['expire_time'],
            ).save()

        except Exception as e:
            # ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '删除成功'}
        try:
            vote_id = json.loads(request.body).get('vote_id', None)
             
            feedbackObj = models.User.objects.get(pk=vote_id)
            if not feedbackObj:
                return JsonResponse({'code': 400, 'msg': 'ID错误'})
            feedbackObj.delete()
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
        return JsonResponse(ret)