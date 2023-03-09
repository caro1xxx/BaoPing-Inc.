from main import models
from main.tools import generateCode6
import json
from main.tools import Validate
from main.views.vote_activity.VoteActivityOp import VoteActivityOp


class VoteTargetOp:
    def checkData(self, name, detail, voteId, count):
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', name, '名称不能为空')
        validate.addCheck('checkIsNotEmpty', detail, '详情不能为空')
        validate.addCheck('checkIsNotEmpty', voteId, '投票ID不能为空')
        validate.addCheck('checkIsNotEmpty', count, '投票ID不能为空')
        ok, msg = validate.startCheck()
        if not ok:
            return ok, msg
        ok, msg = VoteActivityOp().checkVoteIdIsExist(voteId)
        if not ok:
            return ok, msg
        return True, 'ok'
    
    def checkDataOnUpdate(self, name, detail, count, pk):
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', name, 'name不能为空')
        validate.addCheck('checkIsNotEmpty', detail, 'detail不能为空')
        validate.addCheck('checkIsNotEmpty', count, 'count不能为空')
        validate.addCheck('checkIsNotEmpty', pk, 'pk不能为空')
        ok, msg = validate.startCheck()
        if not ok:
            return ok, msg
        ok, msg = self.checkPkIsExist(pk)
        return ok, msg

    def checkPkIsExist(self, pk):
        if models.VoteTarget.objects.filter(pk=pk).first() is None:
            return False, 'pk不存在'
        return True, 'pk重复'

    def create(self, data):
        models.VoteTarget.objects.create(
            vote_id_id = data['vote_id'],
            name = data['name'],
            detail = data['detail'],
            count = data['count']
        )

    # def addMany(self, file):
