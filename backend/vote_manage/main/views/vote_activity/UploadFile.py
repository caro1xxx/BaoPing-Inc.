from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main.views.Common import Common


class UploadFile(APIView):
     def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '添加成功'}
        try:
            filename = Common().uploadFile(request)
            ret['data'] = {'filename': filename}

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)