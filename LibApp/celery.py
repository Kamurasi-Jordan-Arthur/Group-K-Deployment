import os
from celery import Celery
from datetime import timedelta
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibApp')
app = Celery('LibApp')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'Africa/Nairobi'
 
app.conf.beat_schedule = {
    "every_thirty_seconds": {
        "task": "std_app.tasks.thirty_second_func",
        "schedule": timedelta(seconds=30),
    },
}

app.conf.beat_schedule = {
    "notify_borrowers": {
        "task": "std_app.tasks.notify",
        "schedule": timedelta(days=1),
    },
}
 
app.autodiscover_tasks()
 
 # celery -A LibApp.celery beat -l INFO