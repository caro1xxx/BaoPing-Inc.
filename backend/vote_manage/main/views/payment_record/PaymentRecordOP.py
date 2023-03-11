from main import models
from main.tools import Validate
from main.vote_activity.VoteActivityOp import VoteActivityOp


class PaymentRecordOp:
    def create(self, data):
        models.PaymentRecord.objects.create(
            voteuser_id = data['voteuser_open_id'],
            vote_activity_id = data['vote_id'],
            price = data['price'],
            create_time = data['create_time'],
            ip = data['ip'],
            phone_number = data['phone_number'],
            phone_model = data['phone_model'],
            system = data['system'],
            network = data['network'],
            prize_type = data['prize_type'],
            payment_order_id = data['payment_order_id'],
            payment_status = 0
        )

    def updateStatus(self, data):
        models.PaymentRecord.objects.filter(payment_order_id=data['payment_order_id']).update(
            status = data['status']
        )

    def queryOrderIsExist(self, paymentOrderId):
        return models.PaymentRecord.objects.filter(payment_order_id=paymentOrderId).first()

    def checkDataOnCreate(self, data):
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', data['voteuser_open_id'], '用户open_id不能为空')
        validate.addCheck('checkIsNotEmpty', data['vote_id'], '活动参数不能为空')
        validate.addCheck('checkIsNotEmpty', data['price'], '价格不能为空')
        validate.addCheck('checkIsNotEmpty', data['create_time'], '创建时间不能为空')
        validate.addCheck('checkIsNotEmpty', data['ip'], 'ip不能为空')
        validate.addCheck('checkIsNotEmpty', data['phone_number'], '手机号码不能为空')
        validate.addCheck('checkIsNotEmpty', data['phone_model'], '手机型号不能为空')
        validate.addCheck('checkIsNotEmpty', data['system'], '手机系统不能为空')
        validate.addCheck('checkIsNotEmpty', data['network'], '网络不能为空')
        validate.addCheck('checkIsNotEmpty', data['prize_type'], '礼物类型不能为空')
        validate.addCheck('checkIsNotEmpty', data['payment_order_id'], '支付交易号不能为空')
        ok, msg = validate.startCheck()
        if not ok:
            return False, msg
        ok, msg = VoteActivityOp().checkVoteIdIsExist(data['vote_id'])
        if not ko:
            return False, msg
        if models.VoteUser.objects.filter(open_id=data['voteuser_open_id']).first() is None:
            return False, '该用户不存在'
        return True, None

