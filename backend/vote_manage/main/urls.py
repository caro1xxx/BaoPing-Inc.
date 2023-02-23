from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include,re_path
from main.views import Login, Register, ForgetPassword, CheckEmailCode, SendEmailCode, Request404
from vote_manage import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT
    }),
    url(r'^login/$', Login.Login.as_view()),
    url(r'^register/$', Register.Register.as_view()),
    url(r'^forgetpassword/$', ForgetPassword.ForgetPassword.as_view()),
    url(r'^checkemailcode/$', CheckEmailCode.CheckEmailCode.as_view()),
    url(r'^sendemailcode/$', SendEmailCode.SendEmailCode.as_view()),
    url(r'$', Request404.Request404.as_view())
]