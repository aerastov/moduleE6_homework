from django.urls import re_path
from .consumers import WSConsumer


ws_urlpatterns = [
    re_path(r'ws/chat/', WSConsumer.as_asgi()),
    # re_path('ws/chat/', WSConsumer.as_asgi()),
]

channel_routing = {
    'websocket.connect': 'chat_server.consumers.WSConsumer.as_asgi()',
    'websocket.receive': 'chat_server.consumers.WSConsumer.as_asgi()',
    'websocket.disconnect': 'chat_server.consumers.WSConsumer.as_asgi()',
}

# websocket_urlpatterns = [
#     re_path(r'ws/chat/(?P<room_name>\w+)', consumers.ChatRoomConsumer),
# ]

# from channels.routing import route
# from channels import include
# # from chatdemo.consumers import chat_connect, chat_disconnect, chat_receive, loadhistory_connect, loadhistory_disconnect, \
# #     loadhistory_receive
#
# chat_routing = [
#     route("websocket.connect", chat_connect),
#     route("websocket.receive", chat_receive),
#     route("websocket.disconnect", chat_disconnect)
# ]
#
# loadhistory_routing = [
#     route("websocket.connect", loadhistory_connect),
#     route("websocket.receive", loadhistory_receive),
#     route("websocket.disconnect", loadhistory_disconnect)
# ]
#
# channel_routing = [
#     include(chat_routing, path=r"^/ws/$"),
#     include(loadhistory_routing, path=r"^/loadhistory/$"),
# ]