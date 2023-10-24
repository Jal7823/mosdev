from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import ViewPost,ViewCategories



router = DefaultRouter()

router.register(r'', ViewPost,basename='Post')
router.register(r'categorie', ViewCategories,basename='Categories')

urlpatterns = [
        path('',include(router.urls)),
        ]
