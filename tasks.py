from celery import Celery
from time import sleep
from celery_settings import app

# app = Celery('tasks',
#              broker='redis://localhost:6379/',
#              backend='redis://',
#              )


"""
This name task is should be unique
"""
@app.task(name='this-is-just-func')
def add(x, y):
    sleep(5)
    return x + y


@app.task
def mu(x, y):
    return x * y


@app.task
def sub(x, y):
    return x - y


@app.task(bind=True)
def dump_context(self, x, y):
    print('Executing task id {0.id}, '
          'args: {0.args!r} '
          'kwargs: {0.kwargs!r}'.format(
            self.request))
