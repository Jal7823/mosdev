from rest_framework import viewsets
from apps.post.models import Post
from apps.categories.models import Categorie
from .serializers import SerializersPost, SerializersCategories


class ViewPost(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = SerializersPost


class ViewsCategories(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = SerializersCategories

