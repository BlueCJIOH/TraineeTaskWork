from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name="group_membership", blank=True)
    product = models.ForeignKey(
        Product, related_name="groups", on_delete=models.CASCADE
    )
