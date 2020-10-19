import logging
from celery import shared_task


@shared_task
def greeting_task():
    logging.warning('Hello world')
