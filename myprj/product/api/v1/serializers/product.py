from django.db.models import Count, Avg, Max
from rest_framework import serializers

from group.models import Group
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    activity_num = serializers.SerializerMethodField()
    member_num = serializers.SerializerMethodField()
    percent_occupancy = serializers.SerializerMethodField()
    product_rate = serializers.SerializerMethodField()

    class Meta(object):
        model = Product
        fields = "__all__"
        read_only_fields = (
            "activity_num",
            "member_num",
            "percent_occupancy",
            "product_rate",
        )

    def get_activity_num(self, obj):
        return (
            Product.objects.filter(id=obj.id)
            .aggregate(activity_num=Count("activity"))
            .get("activity_num")
        )

    def get_member_num(self, obj):
        return (
            Product.objects.filter(id=obj.id)
            .aggregate(member_num=Count("members"))
            .get("member_num")
        )

    def get_percent_occupancy(self, obj):
        calc_stuff = (
            Group.objects.filter(product_id=obj.id)
            .values("name")
            .annotate(member_num=Count("members", distinct=True))
            .aggregate(Avg("member_num"), Max("member_num"))
        )
        return round(
            (calc_stuff["member_num__avg"] / calc_stuff["member_num__max"]) * 100, 2
        )

    def get_product_rate(self, obj):
        current_obj_num, total_num = Product.objects.filter(id=obj.id).aggregate(
            Count("members")
        ), Product.objects.aggregate(Count("members"))
        return round(
            (current_obj_num["members__count"] / total_num["members__count"]) * 100, 2
        )


class ProductStartSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Product
        fields = ("start_date",)
