from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
  path('admin/', admin.site.urls),
  path('post/', include('apps.post.api.routes')),
  path('publicity/', include('apps.publicity.api.routes')),
  path('categories/', include('apps.categories.api.routes')),
  # YOUR PATTERNS
  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
  path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
  path('', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
