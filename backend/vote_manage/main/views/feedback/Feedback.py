from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
import json

class Feedback(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            value = request.GET.get('value', None)

            if value in ['all', None]:
                feedbackObj =  models.Feedback.objects.all()
            else:
                feedbackObj = models.Feedback.objects.filter(content__contains=value)

            data = []
            for feedback in feedbackObj:
                tmp = {}
                tmp['pk'] = feedback.pk
                tmp['open_id'] = feedback.voteuser.open_id
                tmp['wx_username'] = feedback.voteuser.wx_username
                tmp['avator'] = feedback.voteuser.avator
                tmp['content'] = feedback.content
                tmp['create_time'] = feedback.create_time
                data.append(tmp)
            ret['data'] = data

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'msg': str(e)}
        return JsonResponse(ret)

    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '删除成功'}
        try:
            feedbackId = json.loads(request.body).get('feedback_id', None)
             
            feedbackObj = models.Feedback.objects.get(id=feedbackId)
            if not feedbackObj:
                return JsonResponse({'code': 400, 'msg': 'ID错误'})
            feedbackObj.delete()
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)