from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import generateCode6
import json
from main.tools import Validate
from main.views.vote_activity.VoteActivityOp import VoteActivityOp
from django.core.paginator import Paginator
from vote_manage.settings import BASE_DIR

class TestView(APIView):
    def post(self, request, *args, **kwargs):
        print('test')
        return JsonResponse({})
        try:
            file_obj = request.FILES.get('file')
            import os
            f = open(os.path.join(BASE_DIR, 'static', 'pic', file_obj.name), 'wb')
            print(file_obj,type(file_obj))
            for chunk in file_obj.chunks():
                f.write(chunk)
            f.close()
            print('11111')
            return JsonResponse({})
        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'msg': str(e)}
            return JsonResponse(ret)