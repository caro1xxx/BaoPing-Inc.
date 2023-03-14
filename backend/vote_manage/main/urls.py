from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include,re_path
from main.views.user import Login, Register, ForgetPasswordSendEmail, CheckEmailCode, SendEmailCode, SetNewPassword, UserInfo
from main.views.logs import Logs
from main.views.system_manage import OfficialAccount
from main.views.feedback import Feedback
from main.views.vote_activity import VoteActivity, AloneVoteActivity, UploadFile
from main.views.domain import Domain
from main.views.applyprize import ApplyPrize
from main.views.vote_record import VoteRecord
from main.views.payment_record import PaymentRecord, QueryPayment, QueryPaymentStatus
from main.views.voteuser import Voteuser, Comment
from main.views.statics import Statics, StaticsHistory
from main.views.settings import Settings
from main.views.vote_target import VoteTarget, AddVoteTargets, UpdateVoteTargetStatus
from main.views.gift import Gift
from main.views import Request404, TestView
from main.views.task import Task
from vote_manage import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT
    }),
    url(r'^api/login/$', Login.Login.as_view()),
    url(r'^api/register/$', Register.Register.as_view()),
    url(r'^api/forgetpasswordsendemail/$', ForgetPasswordSendEmail.ForgetPasswordSendEmail.as_view()),
    url(r'^api/checkemailcode/$', CheckEmailCode.CheckEmailCode.as_view()),
    url(r'^api/sendemailcode/$', SendEmailCode.SendEmailCode.as_view()),
    url(r'^api/setnewpassword/$', SetNewPassword.SetNewPassword.as_view()),
    url(r'^api/userinfo/$', UserInfo.UserInfo.as_view()),
    url(r'^api/officialaccount/$', OfficialAccount.OfficialAccount.as_view()),
    url(r'^api/feedback/$', Feedback.Feedback.as_view()),
    url(r'^api/voteactivity/$', VoteActivity.VoteActivity.as_view()),
    url(r'^api/domain/$', Domain.Domain.as_view()),
    url(r'^api/applyprize/$', ApplyPrize.ApplyPrize.as_view()),
    url(r'^api/voterecord/$', VoteRecord.VoteRecord.as_view()),
    url(r'^api/paymentrecord/$', PaymentRecord.PaymentRecord.as_view()),
    url(r'^api/voteuser/$', Voteuser.Voteuser.as_view()),
    url(r'^api/statics/$', Statics.Statics.as_view()),
    url(r'^api/staticshistory/$', StaticsHistory.StaticsHistory.as_view()),
    url(r'^api/logs/$', Logs.Logs.as_view()),
    url(r'^api/settings/$', Settings.Settings.as_view()),
    url(r'^api/alonevoteactivity/$', AloneVoteActivity.AloneVoteActivity.as_view()),
    url(r'^api/votetarget/$', VoteTarget.VoteTarget.as_view()),
    url(r'^api/addvotetargets/$', AddVoteTargets.AddVoteTargets.as_view()),
    url(r'^api/gift/$', Gift.Gift.as_view()),
    url(r'^api/comment/$', Comment.Comment.as_view()),
    url(r'^api/uploadfile/$', UploadFile.UploadFile.as_view()),
    url(r'^api/updatetargetstatus/$', UpdateVoteTargetStatus.UpdateVoteTargetStatus.as_view()),
    url(r'^api/querypayment/$', QueryPayment.QueryPayment.as_view()),
    url(r'^api/query/querypaymentstatus/$', QueryPaymentStatus.QueryPaymentStatus.as_view()),
    url(r'^api/task/$', Task.Task.as_view()),
    url(r'$', Request404.Request404.as_view())
]