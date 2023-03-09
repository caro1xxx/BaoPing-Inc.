from main import models
from main.tools import Validate, getNowTimeStamp


class FeedbackOp:
    def checkDataOnCreate(self, data):
        if data is None:
            return False, '参数错误'

        validate = Validate()
        validate.addCheck('checkIsNotEmpty', data.get('vote_id', None), '活动ID不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('vote_user_open_id', None), '用户ID不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('content', None), '内容ID不能为空')
        ok, msg = validate.startCheck()
        if not ok:
            return False, msg

        if models.VoteActivity.objects.filter(vote_id=data['vote_id']).first() is None:
            return False, '活动不存在'
        if models.VoteUser.objects.filter(open_id=data['vote_user_open_id']).first() is None:
            return False, '该用户不存在'

        return True, None

    def create(self, data):
        models.Feedback.objects.create(
            vote_activity_id = data['vote_id'],
            voteuser_id = data['vote_user_open_id'],
            content = data['content'],
            create_time = getNowTimeStamp()
        )