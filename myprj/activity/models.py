from django.db import models

from product.models import Product


class Activity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    video_url = models.URLField()
