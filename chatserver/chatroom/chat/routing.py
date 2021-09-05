from django.urls import re_path

from . import consumers as cs
from public_chat.consumers import PublicChatConsumer

websocket_urlpatterns = [
    re_path(r'chat/(?P<room_id>\w+)/$', cs.ChatConsumer.as_asgi()),
	re_path(r'public_chat/(?P<room_id>\w+)/$/',PublicChatConsumer.as_asgi()),
]