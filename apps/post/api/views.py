from rest_framework import viewsets
from ..models import Post, Categorie
from .serializers import SerializersPost, SerializersCategories


class ViewPost(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = SerializersPost


class ViewCategories(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = SerializersCategories
