from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from main.views import GetDomain, Active, TestFun, DomainVisCnt

urlpatterns = [
    url(r'getdomain', GetDomain.as_view()),
    url(r'active', Active.as_view()),
    # temp
    url(r'test', TestFun.as_view()),
    url(r'domainviscnt', DomainVisCnt.as_view()),
]