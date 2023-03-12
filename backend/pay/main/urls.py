from django.conf.urls import url
from main.views.wxpay import UserInfo


urlpatterns = [
    url(r'^api/userinfo/$', UserInfo.UserInfo.as_view()),
]