import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.views.user.UserOp import UserOp
from main.tools import *
from main.views.Common import Common
from main.views.task.TaskOp import TaskOp


class Task(APIView):
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            TaskOp().autoUpdateStatus()
            ret['data'], ret['page_count'] = Common().getData(request, 'Task', maxsize=20, desc_order=True)
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
