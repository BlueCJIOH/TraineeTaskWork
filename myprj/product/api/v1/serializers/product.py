from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    activity_num = serializers.SerializerMethodField()

    class Meta(object):
        model = Product
        fields = "__all__"
        read_only_fields = ("activity_num",)

    def get_activity_num(self, obj):
        return obj.activity_set.count()


class ProductStartSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Product
        fields = ("start_date",)
