from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import getNowTimeStamp, myPaginator
from main.views.voteuser.CommentOp import CommentOp
import json


class Comment(APIView):
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

# fix bug
    def delete(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '修改成功'}
        try:
            pk = json.loads(request.body).get('pk', None)

            commentOp = CommentOp()
            ok, msg = commentOp.checkDataOnQuery(pk)
            if not ok:
                return JsonResponse({'code': 400, 'msg': msg})
            
            commentOp.delete(pk)

        except Exception as e:
            ret = {'code': 500, 'msg': 'Timeout'}
            ret = {'code': 500, 'msg': 'Timeout', 'error': str(e)}
        return JsonResponse(ret)