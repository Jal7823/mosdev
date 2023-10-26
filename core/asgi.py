import os
from django.conf import settings
from whitenoise import WhiteNoise
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)