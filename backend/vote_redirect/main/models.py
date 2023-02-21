from django.db import models

# Create your models here.

class domain(models.Model):
    domain = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
