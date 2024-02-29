import datetime

from django.contrib.auth.models import User
from django.db import models

from creator.models import Creator


class Product(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    start_date = models.DateTimeField(default=datetime.datetime.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_members = models.PositiveIntegerField(default=0)
    max_members = models.PositiveIntegerField()
    members = models.ManyToManyField(
        User, related_name="product_membership", blank=True
    )
