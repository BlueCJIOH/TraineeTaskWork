from rest_framework import viewsets

from activity.api.v1.serializers.activity import ActivitySerializer
from activity.models import Activity


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
