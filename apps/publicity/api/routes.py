from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import ViewsPublicity



router = DefaultRouter()

router.register(r'',ViewsPublicity ,basename='Publicity')

urlpatterns = [
        path('',include(router.urls)),
        ]
