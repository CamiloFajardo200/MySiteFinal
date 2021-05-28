"""
ASGI config for MySite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django
from channels.auth import AuthMiddlewareStack

from django.core.asgi import get_asgi_application
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
import game.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MySite.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            game.routing.websocket_urlpatterns
        )
    ),
})
