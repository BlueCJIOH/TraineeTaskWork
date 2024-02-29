from rest_framework import serializers

from activity.models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Activity
        fields = "__all__"
