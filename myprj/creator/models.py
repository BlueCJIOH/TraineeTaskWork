from django.contrib.auth.models import User
from django.db import models

from core.enums import CreatorType


class Creator(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=CreatorType.items())

    def __str__(self):
        return self.name
