from main import models
from main.tools import Validate, getNowTimeStamp


class CommentOp:
    def checkDataOnCreate(self, data):
        if data is None:
            return False, '参数错误'
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', data.get('vote_target_id', None), '选手ID不能为空')
        validate.addCheck('checkIsNumber', data.get('vote_target_id', None), '选手ID格式错误')
        validate.addCheck('checkIsNotEmpty', data.get('vote_user_open_id', None), '用户ID不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('content', None), '评论内容不能为空')
        ok, msg = validate.startCheck()
        if not ok:
            return False, msg
        if models.VoteTarget.objects.filter(pk=data['vote_target_id']).first() is None:
            return False, '该选手不存在'
        if models.VoteUser.objects.filter(open_id=data['vote_user_open_id']).first() is None:
            return False, '该用户不存在'
        return True, None
    
    def create(self, data):
        models.CommentRecord.objects.create(
            vote_target_id = data['vote_target_id'],
            vote_user_id = data['vote_user_open_id'],
            content = data['content'],
            create_time = getNowTimeStamp(),
            status = data.get('status', 0)
        )

    def checkDataOnUpdate(self, data):
        if data is None:
            return False, '参数错误'
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', data.get('pk', None), '评论ID不能为空')
        validate.addCheck('checkIsNumber', data.get('pk', None), '评论ID格式错误')
        ok, msg = validate.startCheck()
        if not ok:
            return False, msg
        if models.CommentRecord.objects.filter(pk=data['pk']).first() is None:
            return False, '评论不存在'
        return True, None
    
    def update(self, data):
        models.CommentRecord.objects.filter(pk=data['pk']).update(status=data['status'])

    def checkDataOnQuery(self, voteTargetId):
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', voteTargetId, '选手ID不能为空')
        validate.addCheck('checkIsNumber', voteTargetId, '选手ID格式错误')
        ok, msg = validate.startCheck()
        if not ok:
            return False, msg
        if models.VoteTarget.objects.filter(pk=voteTargetId).first() is None:
            return False, '选手不存在'
        return True, None
    
    def queryWithVoteActivity(self, voteTargetId):
        return models.CommentRecord.objects.filter(vote_target_id=voteTargetId).exclude(status=0).order_by('create_time')
    
    def all(self):
        return models.CommentRecord.objects.all().order_by('-create_time')

    def checkDataOnDelete(self, pk):
        data = {'pk': pk}
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', data.get('pk', None), '评论ID不能为空')
        validate.addCheck('checkIsNumber', data.get('pk', None), '评论ID格式错误')
        ok, msg = validate.startCheck()
        if not ok:
            return False, msg
        if models.CommentRecord.objects.filter(pk=data['pk']).first() is None:
            return False, '评论不存在'
        return True, None

    def delete(self, pk):
        return models.CommentRecord.objects.filter(pk=pk).delete()