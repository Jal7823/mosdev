from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.categories.api.serializers import SerializersCategories
from apps.post.api.serializers import SerializersPost

from apps.categories.models import Categorie
from apps.post.models import Post


class ViewsetsCategories(viewsets.ModelViewSet):
    serializer_class = SerializersCategories
    queryset = Categorie.objects.all()


@api_view(['GET'])
def get_posts_by_category(request, name):
    try:
        category = Categorie.objects.get(name=name)
        posts = Post.objects.filter(category=category)
        serializer = SerializersPost(posts, many=True)
        return Response(serializer.data)
    except Categorie.DoesNotExist:
        return Response({'message': 'Category not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
