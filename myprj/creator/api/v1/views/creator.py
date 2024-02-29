from rest_framework import viewsets

from creator.api.v1.serializers.creator import CreatorSerializer
from creator.models import Creator


class CreatorViewSet(viewsets.ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
