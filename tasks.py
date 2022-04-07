from celery import Celery
from time import sleep
from celery_settings import app

# app = Celery('tasks',
#              broker='redis://localhost:6379/',
#              backend='redis://',
#              )


@app.task
def add(x, y):
    sleep(5)
    return x + y


@app.task
def mu(x, y):
    return x * y


@app.task
def sub(x, y):
    return x - y
