from rest_framework import serializers

from group.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Group
        fields = "__all__"
