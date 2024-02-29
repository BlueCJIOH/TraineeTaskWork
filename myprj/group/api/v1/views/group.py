from rest_framework import viewsets

from group.api.v1.serializers.group import GroupSerializer
from group.models import Group


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
