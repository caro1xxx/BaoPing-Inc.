import os
from celery import Celery
 
 # 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vote_manage.settings')
 
 # 实例化
# app = Celery('vote_manage')
app = Celery('vote_manage', backend='redis://localhost:6379/1', broker='redis://localhost:6379/0')
 
 # namespace='CELERY'作用是允许你在Django配置文件中对Celery进行配置
 # 但所有Celery配置项必须以CELERY开头，防止冲突
app.config_from_object('django.conf:settings')
 
 # 自动从Django的已注册app中发现任务
app.autodiscover_tasks()
 