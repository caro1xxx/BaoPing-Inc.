from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import getNowTimeStamp, myPaginator
import json
from main.views.voteuser.FeedbackOp import FeedbackOp



class Feedback(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '反馈成功'}
        try:
            data = json.loads(request.body).get('data', None)

            feedbackOp = FeedbackOp()
            ok, msg = feedbackOp.checkDataOnCreate(data)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            
            feedbackOp.create(data)
            ret['data'] = "{}"

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
