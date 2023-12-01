from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewsetsCategories,get_posts_by_category

router = DefaultRouter()

router.register(r'', ViewsetsCategories, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
    path('post-by-category/<str:name>/', get_posts_by_category, name='post-by-category'),
]
