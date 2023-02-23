import json
from main import models
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core import serializers
from django.core.cache import cache
from main.views.UserOp import UserOp
import os


class UploadFile(APIView):
    def post(self, request, *args, **kwargs):
        # return JsonResponse({})
        image = request.FILES.get('image')
        obj = models.User.objects.create(name = 'name', username = 'username', pwd='pwd', create_time = 1231, last_login_time = 123123, email = 'create_time', auth = 1, avator = image, token = 'token', status =1)
        obj.save()
        ret={}
        ret['data'] = str(image)
        return JsonResponse(ret)