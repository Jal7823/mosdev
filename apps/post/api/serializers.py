from rest_framework import serializers
from apps.post.models import Categorie,Post


class SerializersCategories(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class SerializersPost(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = SerializersCategories(many=True)

    class Meta:
        model = Post
        fields = '__all__'
