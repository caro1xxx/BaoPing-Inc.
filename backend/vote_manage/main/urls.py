from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from main.views import Login, Register

urlpatterns = [
    url(r'login', Login.Login.as_view()),
    url(r'register', Register.Register.as_view()),
]