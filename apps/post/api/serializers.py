from rest_framework import serializers
from ..models import Post, Categorie


class SerializersPost(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'


class SerializersCategories(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
