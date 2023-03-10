from main import models
from main.tools import Validate
from main.tools import getNowTimeStamp, getIp, getLocationFromIp, getTodayBeginTimeStamp
from django.db.models import F, Q, Count
from main.views.BlankListOp import BlankListOp


class SupportOp:
    def checkOpenidIsExist(self, open_id):
        if models.VoteUser.objects.filter(open_id=open_id).first() is None:
            return False, 'openoid不存在'
        return True, None

    def checkVoteTargetIsExist(self, voteTargetId):
        if models.VoteTarget.objects.filter(pk=voteTargetId).first() is None:
            return False, '投票对象不存在'
        return True, None
    
    def checkVoteIsExist(self, voteId):
        if models.VoteActivity.objects.filter(vote_id=voteId).first() is None:
            return False, '投票活动不存在'
        return True, None

    def checkSettingsOnCreate(self, data):
        location = getLocationFromIp(data['ip'])
        voteActivity = models.VoteActivity.objects.filter(vote_id=data['vote_id']).first()
        settingsRegion = voteActivity.allowed_vote_region
        if settingsRegion not in ['全国', location['city']] or location['city'] != 'other':
            return False, '暂不支持您所在地区投票'
        
        blankListOp = BlankListOp()
        if blankListOp.checkVoteUserIsExist(data['open_id']):
            return False, '该用户已进入黑名单'
        if blankListOp.checkIpIsExist(data['ip']):
            return False, '该ip已进入黑名单'
        
        nowTime = getNowTimeStamp()
        todayBeginTime = getTodayBeginTimeStamp(nowTime)
        lastHourTime = nowTime - 3600

        user_vote_count_day = models.VoteRecord.objects.filter(
            Q(voteuser_id = data['open_id']) &
            Q(vote_activity_id = data['vote_id']) &
            Q(create_time__gte = todayBeginTime) &
            Q(create_time__lt = nowTime)
        ).aggregate(cnt=Count('create_time'))['cnt']
        if user_vote_count_day >= voteActivity.allowed_alone_everyday_vote_count:
            return False, '今日投票数量已到上限'

        user_vote_count_hour = models.VoteRecord.objects.filter(
            Q(voteuser_id = data['open_id']) &
            Q(vote_activity_id = data['vote_id']) &
            Q(create_time__gte = lastHourTime) &
            Q(create_time__lt = nowTime)
        ).aggregate(cnt=Count('create_time'))['cnt']
        if user_vote_count_hour >= voteActivity.allowed_alone_everyhour_vote_count:
            return False, '每小时投票数量已到上限'
        return True, None

    def checkDataOnCreate(self, data):
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', data.get('open_id', None), 'openid不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('vote_target_id', None), '投票对象不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('vote_id', None), '活动不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('phone_model', None), '手机型号不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('system', None), '设备系统不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('network', None), '网络不能为空')
        ok, msg = validate.startCheck()
        if not ok:
            return ok, msg
        ok, msg = self.checkOpenidIsExist(data['open_id'])
        if not ok:
            return ok, msg
        ok, msg = self.checkVoteTargetIsExist(data['vote_target_id'])
        if not ok:
            return ok, msg
        ok, msg = self.checkVoteIsExist(data['vote_id'])
        if not ok:
            return ok, msg
        return True, None
    
    def create(self, data, request):
        models.VoteRecord.objects.create(
                voteuser_id = data['open_id'],
                vote_target_id = data['vote_target_id'],
                create_time = getNowTimeStamp(),
                vote_activity_id = data['vote_id'],
                ip = data['ip'],
                phone_model = data['phone_model'],
                system = data['system'],
                network = data['network'],
        ).save()
        models.VoteTarget.objects.filter(pk=data['vote_target_id']).update(
                count = F('count') + 1
        )