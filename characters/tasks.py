from celery import shared_task

from app.scrapper import sync_characters

from .models import Character

@shared_task
def characters_count():
    return Character.objects.count()

@shared_task
def run_characters_sync():
    return sync_characters()
