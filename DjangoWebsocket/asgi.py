"""
ASGI config for DjangoWebsocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from apps.routing import websocket_urlpatterns



application = get_asgi_application()

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from apps.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoWebsocket.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # Oddiy Django HTTP so‘rovlarini qabul qilish
        "websocket": AuthMiddlewareStack(  # WebSocket ulanishlarini boshqarish
            URLRouter(websocket_urlpatterns)
        ),
    }
)

