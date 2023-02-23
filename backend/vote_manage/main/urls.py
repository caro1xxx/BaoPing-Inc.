from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from main.views import Login, Register, ForgetPassword, CheckEmailCode, SendEmailCode

urlpatterns = [
    url(r'login', Login.Login.as_view()),
    url(r'register', Register.Register.as_view()),
    url(r'forgetpassword', ForgetPassword.ForgetPassword.as_view()),
    url(r'checkemailcode', CheckEmailCode.CheckEmailCode.as_view()),
    url(r'sendemailcode', SendEmailCode.SendEmailCode.as_view()),
]