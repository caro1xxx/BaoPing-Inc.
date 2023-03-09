from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse
from main import models
from main.tools import generateCode6
import json
from main.tools import Validate


class VoteActivityOp:
    def checkVoteIdIsExist(self, voteId):
        if models.VoteActivity.objects.filter(vote_id=voteId).first() is None:
            return False, '该活动不存在'
        return True, '活动ID重复'
    
    def checkVoteuserIsExist(self, voteuserOpen_id):
        if models.VoteUser.objects.filter(open_id=voteuserOpen_id).first() is None:
            return False, '该用户不存在'
        return True, '用户名重复'

    def checkActivityData(self, data):
        ok, msg = self.checkVoteIdIsExist(data.get('vote_id', None))
        if not ok:
            return False, msg
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', data.get('vote_everyday_begin_time', None), '每日投票开始时间不能为空')
        # validate.addCheck('checkIsNumber', data.get('vote_everyday_begin_time', None), '每日投票开始时间错误')
        validate.addCheck('checkIsNotEmpty', data.get('vote_everyday_end_time', None), '每日投票结束时间不能为空')
        # validate.addCheck('checkIsNumber', data.get('vote_everyday_end_time', None), '每日投票结束时间错误')
        validate.addCheck('checkIsNotEmpty', data.get('vote_enroll_begin_time', None), '报名时间不能为空')
        validate.addCheck('checkIsNumber', data.get('vote_enroll_begin_time', None), '报名时间错误')
        validate.addCheck('checkIsNotEmpty', data.get('vote_enroll_end_time', None), '结束投票时间不能为空')
        validate.addCheck('checkIsNumber', data.get('vote_enroll_end_time', None), '结束投票时间错误')
        validate.addCheck('checkIsNotEmpty', data.get('allowed_vote_region', None), '区域不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('visit_count', None), '浏览量不能为空')
        validate.addCheck('checkIsNumber', data.get('visit_count', None), '浏览量错误')
        validate.addCheck('checkIsNotNagetiveNumber', data.get('visit_count', None), '浏览量不能为负数')
        validate.addCheck('checkIsNotEmpty', data.get('visit_count_multiple', None), '浏览倍数不能为空')
        validate.addCheck('checkIsNumber', data.get('visit_count_multiple', None), '浏览倍数错误')
        validate.addCheck('checkIsNotNagetiveNumber', data.get('visit_count_multiple', None), '浏览倍数不能为负数')
        ok, msg = validate.startCheck()
        return ok, msg
    
    def checkVoteData(self, data):
        ok, msg = self.checkVoteIdIsExist(data.get('vote_id', None))
        if not ok:
            return False, msg
        if data.get('today_start_voteuser_open_id', None) not in ['', None]:
            ok, msg = self.checkVoteuserIsExist(data.get('today_start_voteuser_open_id', None))
            if not ok:
                return ok, msg
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', data.get('today_star_update_begin_time', None), '今日之星开始时间不能为空')
        # validate.addCheck('checkIsNumber', data.get('today_star_update_begin_time', None), '今日之星开始时间错误')
        validate.addCheck('checkIsNotEmpty', data.get('today_star_update_end_time', None), '今日之星结束时间不能为空')
        # validate.addCheck('checkIsNumber', data.get('today_star_update_end_time', None), '今日之星结束时间错误')
        validate.addCheck('checkIsNotEmpty', data.get('allowed_alone_everyday_vote_count', None), '单人每日投票上限不能为空')
        validate.addCheck('checkIsNumber', data.get('allowed_alone_everyday_vote_count', None), '单人每日投票上限错误')
        validate.addCheck('checkIsNotEmpty', data.get('allowed_alone_everyhour_vote_count', None), '单人每小时投票上限不能为空')
        validate.addCheck('checkIsNumber', data.get('allowed_alone_everyhour_vote_count', None), '单人每小时投票上限时间错误')
        validate.addCheck('checkIsNotEmpty', data.get('open_today_star_with', None), '第几天显示今日之星不能为空')
        validate.addCheck('checkIsNumber', data.get('open_today_star_with', None), '第几天显示今日之星错误')
        validate.addCheck('checkIsNotEmpty', data.get('visible_no1_with', None), '第几天显示第一名不能为空')
        validate.addCheck('checkIsNumber', data.get('visible_no1_with', None), '第几天显示第一名错误')
        validate.addCheck('checkIsNotEmpty', data.get('enable_vote_to_me', None), '是否可以给自己投票不能为空')
        validate.addCheck('checkIsNumber', data.get('enable_vote_to_me', None), '是否可以给自己投票错误')
        validate.addCheck('checkIsNotEmpty', data.get('enable_comment', None), '是否可以评论不能为空')
        validate.addCheck('checkIsNumber', data.get('enable_comment', None), '是否可以评论错误')
        validate.addCheck('checkIsNotEmpty', data.get('enable_vote_cert_code', None), '是否开启投票验证码不能为空')
        validate.addCheck('checkIsNumber', data.get('enable_vote_cert_code', None), '是否开启投票验证码错误')
        validate.addCheck('checkIsNotEmpty', data.get('enable_prize', None), '是否可以送礼物不能为空')
        validate.addCheck('checkIsNumber', data.get('enable_prize', None), '是否可以送礼物错误')
        validate.addCheck('checkIsNotEmpty', data.get('enable_browser', None), '是否可以从浏览器打开不能为空')
        validate.addCheck('checkIsNumber', data.get('enable_browser', None), '是否可以从浏览器打开错误')
        ok, msg = validate.startCheck()
        return ok, msg
        if not ok:
            return ok, msg
        ok, msg = self.checkVoteuserIsExist(data.get('auto_comment_voteuser_open_id', None))
        return ok, msg
    
    def checkAutoCommentData(self, data):
        ok, msg = self.checkVoteIdIsExist(data.get('vote_id', None))
        if not ok:
            return False, msg
        if data.get('auto_comment_voteuser_open_id', None) in ['', None]:
            return True, None
        
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', data.get('auto_comment_voteuser_open_id', None), '自动评论对象用户不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('auto_comment_begin_time', None), '自动评论开始时间不能为空')
        validate.addCheck('checkIsNumber', data.get('auto_comment_begin_time', None), '自动评论开始时间错误')
        validate.addCheck('checkIsNotEmpty', data.get('auto_comment_end_time', None), '自动评论结束时间不能为空')
        validate.addCheck('checkIsNumber', data.get('auto_comment_end_time', None), '自动评论结束时间错误')
        validate.addCheck('checkIsNotEmpty', data.get('auto_comment_everyday_begin_time', None), '自动评论每日开始时间不能为空')
        validate.addCheck('checkIsNumber', data.get('auto_comment_everyday_begin_time', None), '自动评论每日开始时间错误')
        validate.addCheck('checkIsNotEmpty', data.get('auto_comment_everyday_end_time', None), '自动评论每日结束时间不能为空')
        validate.addCheck('checkIsNumber', data.get('auto_comment_everyday_end_time', None), '自动评论每日结束时间错误')
        validate.addCheck('checkIsNotEmpty', data.get('auto_comment_space_minute', None), '自动评论间隔时间不能为空')
        validate.addCheck('checkIsNumber', data.get('auto_comment_space_minute', None), '自动评论间隔时间错误')
        validate.addCheck('checkIsNotEmpty', data.get('auto_comment_everyday_count_strict', None), '自动评论每日上限不能为空')
        validate.addCheck('checkIsNumber', data.get('auto_comment_everyday_count_strict', None), '自动评论每日上限错误')
        ok, msg = validate.startCheck()
        if not ok:
            return ok, msg
        ok, msg = self.checkVoteuserIsExist(data.get('auto_comment_voteuser_open_id', None))
        return ok, msg
    
    def checkTemplateData(self, data):
        ok, msg = self.checkVoteIdIsExist(data.get('vote_id', None))
        if not ok:
            return False, msg
        validate = Validate()
        validate.addCheck('checkIsNotEmpty', data.get('template_id', None), '模版ID不能为空')
        validate.addCheck('checkIsNumber', data.get('template_id', None), '模版ID错误')
        validate.addCheck('checkIsNotEmpty', data.get('description', None), '描述不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('enterprises', None), '企业不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('prize', None), '奖品不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('contact', None), '联系方式不能为空')
        validate.addCheck('checkIsNotEmpty', data.get('support', None), '支持方式不能为空')
        ok, msg = validate.startCheck()
        return ok, msg

    def updateActivityData(self, data):
        voteActivityObj = models.VoteActivity.objects.filter(vote_id=data.get('vote_id', None)).first()
        voteActivityObj.vote_everyday_begin_time = data.get('vote_everyday_begin_time', None)
        voteActivityObj.vote_everyday_end_time = data.get('vote_everyday_end_time', None)
        voteActivityObj.vote_enroll_begin_time = data.get('vote_enroll_begin_time', None)
        voteActivityObj.vote_enroll_end_time = data.get('vote_enroll_end_time', None)
        voteActivityObj.allowed_vote_region = data.get('allowed_vote_region', None)
        voteActivityObj.visit_count = data.get('visit_count', None)
        voteActivityObj.visit_count_multiple = data.get('visit_count_multiple', None)
        voteActivityObj.save()

    def updateVoteData(self, data):
        voteActivityObj = models.VoteActivity.objects.filter(vote_id=data.get('vote_id', None)).first()
        voteActivityObj.vote_count_restrict = data.get('vote_count_restrict', None)
        if data.get('today_start_voteuser_open_id', None) or data.get('today_start_voteuser_open_id', None) != '':
            voteActivityObj.today_start_voteuser = data.get('today_start_voteuser_open_id', None)
            voteActivityObj.today_star_update_begin_time = data.get('today_star_update_begin_time', None)
            voteActivityObj.today_star_update_end_time = data.get('today_star_update_end_time', None)
            voteActivityObj.allowed_alone_everyday_vote_count = data.get('allowed_alone_everyday_vote_count', None)
            voteActivityObj.allowed_alone_everyhour_vote_count = data.get('allowed_alone_everyhour_vote_count', None)
            voteActivityObj.open_today_star_with = data.get('open_today_star_with', None)
        voteActivityObj.visible_no1_with = data.get('visible_no1_with', None)
        voteActivityObj.enable_vote_to_me = data.get('enable_vote_to_me', None)
        voteActivityObj.enable_comment = data.get('enable_comment', None)
        voteActivityObj.enable_vote_cert_code = data.get('enable_vote_cert_code', None)
        voteActivityObj.enable_prize = data.get('enable_prize', None)
        voteActivityObj.enable_browser = data.get('enable_browser', None)
        voteActivityObj.save()

    def updateAutoCommentData(self, data):
        voteActivityObj = models.VoteActivity.objects.filter(vote_id=data.get('vote_id', None)).first()
        if data.get('auto_comment_voteuser_open_id', None) or data.get('auto_comment_voteuser_open_id', None) != '':
            voteActivityObj.auto_comment_voteuser = data.get('auto_comment_voteuser_open_id', None)
            voteActivityObj.auto_comment_begin_time = data.get('auto_comment_begin_time', None)
            voteActivityObj.auto_comment_end_time = data.get('auto_comment_end_time', None)
            voteActivityObj.auto_comment_everyday_begin_time = data.get('auto_comment_everyday_begin_time', None)
            voteActivityObj.auto_comment_everyday_end_time = data.get('auto_comment_everyday_end_time', None)
            voteActivityObj.auto_comment_space_minute = data.get('auto_comment_space_minute', None)
            voteActivityObj.auto_comment_everyday_count_strict = data.get('auto_comment_everyday_count_strict', None)
            voteActivityObj.save()

    def updateTemplateData(self, data):
        voteActivityObj = models.VoteActivity.objects.filter(vote_id=data.get('vote_id', None)).first()
        voteActivityObj.template_id = data.get('template_id', None)
        voteActivityObj.description = data.get('description', None)
        voteActivityObj.enterprises = data.get('enterprises', None)
        voteActivityObj.prize = data.get('prize', None)
        voteActivityObj.contact = data.get('contact', None)
        voteActivityObj.support = data.get('support', None)
        voteActivityObj.save()

    def queryAllVoteuser(self, vote_id):
        voteuserObj = models.VoteUser.objects.filter(voteactivity__vote_id=vote_id).distinct()
        return voteuserObj
    
    def queryAllPayment(self, vote_id):
        paymentRecordObj = models.PaymentRecord.objects.filter(vote_activity_id=vote_id)
        return paymentRecordObj
