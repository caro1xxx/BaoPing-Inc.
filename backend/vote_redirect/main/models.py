from django.db import models

# Create your models here.

class domain(models.Model):
    domain_name = models.CharField(max_length=50, unique=True)
    status = models.IntegerField(default=0)
    visit_count = models.IntegerField(default=0)
    expire_time = models.IntegerField()
    flow = models.IntegerField()
    vote_id = models.IntegerField()
