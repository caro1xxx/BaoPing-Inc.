from main import models
from main.tools import generateCode6
import json
from main.tools import Validate, getNowTimeStamp
from django.db.models import Q


class TaskOp:
    def create(self, name):
        taskId = generateCode6()
        models.Task.objects.create(
            task_id = taskId,
            name = name,
            status = 0,
            msg = 'loading',
            create_time = getNowTimeStamp()
        )
        return taskId

    def updateStatus(self, taskId, status, message):
        models.Task.objects.filter(task_id=taskId).update(
            status = 1 if message == 'success' else 2,
            msg = message
        )
    
    def autoUpdateStatus(self):
        models.Task.objects.filter(
            Q(status = 0) &
            Q(create_time__lt = getNowTimeStamp() - 60)
        ).update(
            status = 2,
            msg = 'failed'
        )