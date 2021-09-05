from channels.auth import AuthMiddlewareStack
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.conf.urls import url
from django.urls import  re_path
from django.core.asgi import get_asgi_application
import chat.routing

from chat.consumers import ChatConsumer
from public_chat.consumers import PublicChatConsumer




os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatroom.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})