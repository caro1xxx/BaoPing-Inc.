from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import getNowTimeStamp, myPaginator
from main.views.voteuser.CommentOp import CommentOp
import json


# 管理员进行评论管理
class Comment(APIView):
    # 获取某活动的全部评论按照发布时间降序
    def get(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': 'ok'}
        try:
            voteId = request.GET.get('vote_id', None)

            commentOp = CommentOp()
            ok, msg = commentOp.checkDataOnQuery(voteId)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            
            data = commentOp.queryWithVoteActivity(voteId)
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
        return JsonResponse(ret)

    # 修改评论状态
    def put(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            data = json.loads(request.body).get('data', None)

            commentOp = CommentOp()
            ok, msg = commentOp.checkDataOnUpdate(data)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            
            commentOp.update(data)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)

    # 删除评论
    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            pk = json.loads(request.body).get('pk', None)

            commentOp = CommentOp()
            ok, msg = commentOp.checkDataOnDelete(pk)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            
            commentOp.delete(pk)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            # ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)