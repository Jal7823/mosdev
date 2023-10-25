from rest_framework import viewsets
from ..models import Publicity
from .serializers import SerializerPublicity


class ViewsPublicity(viewsets.ModelViewSet):
    queryset = Publicity.objects.all()
    serializer_class = SerializerPublicity
