from django.db import models

# Create your models here.

class domain(models.Model):
    domain = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
    vis_cnt = models.IntegerField(default=0)

class Active(models.Model):
    domain_list = models.CharField(max_length=100)
