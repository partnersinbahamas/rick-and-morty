from celery import shared_task

from .models import Character

@shared_task
def characters_count():
    return Character.objects.count()
