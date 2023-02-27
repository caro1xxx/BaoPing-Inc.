from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    pwd = models.CharField(max_length=64)
    create_time = models.IntegerField()
    last_login_time = models.IntegerField()
    email = models.CharField(max_length=50, unique=True)
    # 0: admin, 1: guest
    auth = models.IntegerField(default=1)
    avator = models.TextField(max_length=10, default='22')
    token = models.CharField(max_length=32)
    # 1: 正常 0: 其他
    status = models.IntegerField(default=1)

    # objects = models.Manager()

class Token(models.Model):
    value = models.CharField(max_length=32,unique=True)
    expire_time = models.IntegerField()


class Logs(models.Model):
    who = models.CharField(max_length=20)
    action = models.TextField(max_length=20)
    target = models.TextField(max_length=20, null=False)
    create_time = models.IntegerField(null=False)


class OfficialAccount(models.Model):
    name = models.TextField()
    app_id = models.TextField()
    region = models.TextField()
    wx_pay_pos_id = models.TextField()
    wx_pay_apiv2_secret_key = models.TextField()
    wx_pay_apiv3_secret_key = models.TextField()


class VoteUser(models.Model):
    open_id = models.CharField(unique=True, max_length=128)
    wx_username = models.TextField()
    create_time = models.IntegerField(null=False)