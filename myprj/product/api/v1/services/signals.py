from django.db.models.signals import post_save
from django.dispatch import receiver

from group.models import Group
from product.models import Product


@receiver(post_save, sender=Product)
def client_post_save_receiver(instance, created, *args, **kwargs):
    if created:
        Group.objects.bulk_create(
            [
                Group(
                    product_id=instance.id,
                    name=f"{instance.name}_{len(Group.objects.all()) + cnt}",
                )
                for cnt in range(1, 3)
            ]
        )
