from celery import shared_task


@shared_task
def myTask():
    print('this is selery test')
