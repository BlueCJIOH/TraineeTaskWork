from rest_framework import serializers

from creator.models import Creator


class CreatorSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Creator
        fields = "__all__"
