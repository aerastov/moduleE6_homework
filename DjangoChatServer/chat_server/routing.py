from django.urls import re_path
from .consumers import WSConsumer, ChatConsumer


ws_urlpatterns = [
    re_path(r'ws/chat/\d+/', ChatConsumer.as_asgi()),
    re_path(r'ws/chat/', WSConsumer.as_asgi()),
]


# websocket_urlpatterns = [
#     re_path(r'ws/chat/(?P<room_name>\w+)', consumers.ChatRoomConsumer),
# ]