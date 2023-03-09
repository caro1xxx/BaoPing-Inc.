from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import getNowTimeStamp, myPaginator
from main.views.voteuser.CommentOp import CommentOp
import json


# 用户进行评论操作
class Comment(APIView):
    # 查看某活动的全部评论按照时间升序
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            voteTargetId = request.GET.get('vote_target_id', None)

            commentOp = CommentOp()
            ok, msg = commentOp.checkDataOnQuery(voteTargetId)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            
            data = commentOp.queryWithVoteActivity(voteTargetId)
            data, ret['page_count'] =  myPaginator(data, 20)
            ret['data'] = serializers.serialize('json', data)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    # 发布一条评论
    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '添加成功'}
        try:
            data = json.loads(request.body).get('data', None)

            commentOp = CommentOp()
            ok, msg = commentOp.checkDataOnCreate(data)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            
            commentOp.create(data)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)
