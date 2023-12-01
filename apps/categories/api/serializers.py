from rest_framework import serializers

from apps.categories.models import Categorie


class SerializersCategories(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
