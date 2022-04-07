from celery import Celery

# app = Celery('tasks', broker='redis://',)
app = Celery('tasks',
             broker='redis://',
             backend='redis://',
             )

app.conf.update(result_expires=3600, )

if __name__ == '__main__':
    app.start()
