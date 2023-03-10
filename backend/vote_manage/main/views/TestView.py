from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import generateCode6, getLocationFromIp
import json
from main.tools import Validate
from main.views.vote_activity.VoteActivityOp import VoteActivityOp
from django.core.paginator import Paginator
from vote_manage.settings import BASE_DIR
import geoip2.database
from vote_manage import settings
from main.tasks import myTask, sendEmail
from vote_manage import settings
from openpyxl import load_workbook
from main.views.vote_target.VoteTargetOp import VoteTargetOp
from main.views.Common import Common


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        ret = {}
        try:
            ip = request.GET.get('ip', None)
            location = getLocationFromIp(ip)
            # print(location)
        except Exception as e:
            ret['msg'] = str(e)

        return JsonResponse(ret)
    
    def post(self, request, *args, **kwargs):
        ret = {'code': 200}
        try:
            commonOp = Common()
            filename = commonOp.uploadFile(request)
            ret['filename'] = filename

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'msg': str(e)}
        return JsonResponse(ret)

    def put(self, request, *args, **kwargs):
        ret = {'code': 200}
        try:
            data = {}
            data['vote_id'] = request.POST.get('vote_id', None)
            data['top_roll_text'] = request.POST.get('top_roll_text', None)
            data['start_adv_img'] = request.FILES.get('start_adv_img', None)
            data['bottom_text'] = request.POST.get('bottom_text', None)
            data['video_adv'] = request.FILES.get('video_adv', None)

            voteActivityObj = models.VoteActivity.objects.filter(vote_id=data.get('vote_id', None)).first()
            voteActivityObj.top_roll_text = data['top_roll_text']
            voteActivityObj.start_adv_img = data['start_adv_img']
            voteActivityObj.bottom_text = data['bottom_text']
            voteActivityObj.video_adv = data['video_adv']
            voteActivityObj.save()

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'msg': str(e)}
        return JsonResponse(ret)