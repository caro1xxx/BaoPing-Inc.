from main import models
from main.tools import Validate


class VoteUserOp:
    def checkOpenidIsNotExist(self, open_id):
        if models.VoteUser.objects.filter(open_id=open_id).first() is None:
            return True, 'openoid不存在'
        return False, 'openid已经存在'

    def checkDataOnCreate(self, open_id, wx_username, avator):
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', open_id, 'openid不能为空')
        validate.addCheck('checkIsNotEmpty', wx_username, '微信用户名不能为空')
        validate.addCheck('checkIsNotEmpty', avator, '头像不能为空')
        ok, msg = validate.startCheck()
        if not ok:
                return ok, msg
        ok, msg = self.checkOpenidIsNotExist(open_id)
        return ok, msg
