from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from main.views import GetDomain

urlpatterns = [
    url(r'getdomain', GetDomain.as_view()),
]