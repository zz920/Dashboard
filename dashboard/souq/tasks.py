from celery import shared_task
from souq.models import *


@shared_task
def process_pack_item(data):
    print(data)
