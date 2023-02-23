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
    avator = models.FileField(blank=True, null=True, upload_to='avator', verbose_name='头像')
    token = models.CharField(max_length=32)
    # 1: 正常 0: 其他
    status = models.IntegerField(default=1)

    # objects = models.Manager()