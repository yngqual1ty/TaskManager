from django.utils import timezone
from celery import shared_task
from .models import Task

@shared_task
def mark_overdue_tasks():
    now = timezone.now()
    tasks = Task.objects.filter(deadline__lt=now, is_completed=False, is_overdue=False)
    updated = tasks.update(is_overdue=True)
    return f"{updated} tasks marked as overdue"