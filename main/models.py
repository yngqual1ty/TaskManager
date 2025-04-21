from django.contrib.auth.models import AbstractUser
from django.db import models

from django.core.exceptions import ValidationError

from django.utils import timezone

from django.conf import settings


def validate_date(date):
    if date < timezone.now():
        raise ValidationError('Введите возможный дедлайн!')

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(default='Middle', max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True, null=True, validators=[validate_date])
    is_overdue = models.BooleanField(default=False)

    def __str__(self):
        return self.title



