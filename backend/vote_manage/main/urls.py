from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include,re_path
from main.views.user import Login, Register, ForgetPasswordSendEmail, CheckEmailCode, SendEmailCode, SetNewPassword, UserInfo
from main.views.logs import Logs
from main.views.system_manage import OfficialAccount
from main.views.feedback import Feedback
from main.views.vote_activity import VoteActivity
from main.views.domain import Domain
from main.views.applyprize import ApplyPrize
from main.views.vote_record import VoteRecord
from main.views.payment_record import PaymentRecord
from main.views.voteuser import Voteuser
from main.views.statics import Statics
from main.views.settings import Settings
from main.views import Request404, TestView
from vote_manage import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT
    }),
    url(r'^login/$', Login.Login.as_view()),
    url(r'^register/$', Register.Register.as_view()),
    url(r'^forgetpasswordsendemail/$', ForgetPasswordSendEmail.ForgetPasswordSendEmail.as_view()),
    url(r'^checkemailcode/$', CheckEmailCode.CheckEmailCode.as_view()),
    url(r'^sendemailcode/$', SendEmailCode.SendEmailCode.as_view()),
    url(r'^setnewpassword/$', SetNewPassword.SetNewPassword.as_view()),
    url(r'^userinfo/$', UserInfo.UserInfo.as_view()),
    url(r'^officialaccount/$', OfficialAccount.OfficialAccount.as_view()),
    url(r'^feedback/$', Feedback.Feedback.as_view()),
    url(r'^voteactivity/$', VoteActivity.VoteActivity.as_view()),
    url(r'^domain/$', Domain.Domain.as_view()),
    url(r'^applyprize/$', ApplyPrize.ApplyPrize.as_view()),
    url(r'^voterecord/$', VoteRecord.VoteRecord.as_view()),
    url(r'^paymentrecord/$', PaymentRecord.PaymentRecord.as_view()),
    url(r'^voteuser/$', Voteuser.Voteuser.as_view()),
    url(r'^statics/$', Statics.Statics.as_view()),
    url(r'^logs/$', Logs.Logs.as_view()),
    url(r'^settings/$', Settings.Settings.as_view()),
    url(r'^test/$', TestView.TestView.as_view()),
    url(r'$', Request404.Request404.as_view())
]