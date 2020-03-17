from celery import Celery
from clickpost.tasks import send_notification_message
from celery.schedules import crontab

app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(crontab(hour=19, minute=30), send_notification_message.s(), name='send Notifications')
