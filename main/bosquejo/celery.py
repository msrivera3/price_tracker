import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bosquejo.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('bosquejo')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(["bosquejo"])


# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'mi-tarea-cada-10-segundos': {
        'task': 'bosquejo.tasks.prueba',
        'schedule': 85.0,
    },
}