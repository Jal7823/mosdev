from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ViewPost, ViewsCategories

router = DefaultRouter()

router.register(r'', ViewPost, basename='Post')
router.register(r'categorie', ViewsCategories, basename='Categorie')

urlpatterns = [
    path('', include(router.urls)),
]
