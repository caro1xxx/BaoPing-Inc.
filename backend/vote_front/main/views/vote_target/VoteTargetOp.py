from main import models
from main.tools import generateCode6
import json
from main.tools import Validate


class VoteTargetOp:
    def checkDataOnCreate(self, name, detail, voteId):
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', name, '名称不能为空')
        validate.addCheck('checkIsNotEmpty', detail, '详情不能为空')
        validate.addCheck('checkIsNotEmpty', voteId, '投票ID不能为空')
        ok, msg = validate.startCheck()
        if not ok:
            return ok, msg
        ok, msg = self.checkVoteIsExist(voteId)
        if not ok:
            return ok, msg
        return True, 'ok'
    
    def checkDataOnUpdate(self, name, detail, pk):
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', name, 'name不能为空')
        validate.addCheck('checkIsNotEmpty', detail, 'detail不能为空')
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
    
    def checkVoteIsExist(self, voteId):
        if models.VoteActivity.objects.filter(vote_id=voteId).first() is None:
            return False, '该活动不存在'
        return True, None