from django.db import models
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.username, filename)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return self.username