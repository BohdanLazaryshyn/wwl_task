import os

from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wwl_task.settings')
app = Celery('wwl_task')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    "every_thirty_seconds": {
        "task": "producer.tasks.add_new_order",
        "schedule": timedelta(seconds=60),
    },
}

app.autodiscover_tasks()
