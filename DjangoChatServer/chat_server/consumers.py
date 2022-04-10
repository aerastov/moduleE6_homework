import json
# Импорт для асинхронного программирования
from channels.generic.websocket import AsyncWebsocketConsumer
# Импорт для работы с БД в асинхронном режиме
from channels.db import database_sync_to_async
# Импорт модели сообщений
from .models import Message


from channels.generic.websocket import WebsocketConsumer
from random import randint
from time import sleep


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("СООБЩЕНИЕ", self.scope)
        print('username:', self.scope["path"])
        # iduser = self.kwargs.get('pk')
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        await self.send(json.dumps({'message': self.scope["path"]}))



class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({'message': randint(1, 100)}))
            sleep(1)


    # Метод для отключения пользователя
    # async def disconnect(self, close_code):
        # # Отключаем пользователя
        # await self.channel_layer.group_discard(
        #     self.room_group_name,
        #     self.channel_name
        # )

    # Декоратор для работы с БД в асинхронном режиме
    # @database_sync_to_async
    # # Функция для создания нового сообщения в БД
    # def new_message(self, message):
    #     # Создаём сообщение в БД
    #     Message.objects.create(text=message)
    #
    # # Принимаем сообщение от пользователя
    # async def receive(self, text_data=None, bytes_data=None):
    #     # Форматируем сообщение из JSON
    #     text_data_json = json.loads(text_data)
    #     # Получаем текст сообщения
    #     message = text_data_json['message']
    #
    #     # Добавляем сообщение в БД
    #     await self.new_message(message=message)
    #
    #     # Отправляем сообщение
    #     await self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message,
    #         }
    #     )
    #
    # # Метод для отправки сообщения клиентам
    # async def chat_message(self, event):
    #     # Получаем сообщение от receive
    #     message = event['message']
    #     # Отправляем сообщение клиентам
    #     await self.send(text_data=json.dumps({
    #         'message': message,
    #     }, ensure_ascii=False))































# "Пример от студента
# from channels.generic.websocket import AsyncWebsocketConsumer

# class ChatRoomConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         await self.accept()
#
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'test_message',
#                 'tester': 'hello',
#             }
#         )
#
#     async def tester_message(self, event):
#         tester = event['tester']
#
#         await self.send(text_data=json.dumps({
#             'tester': tester
#         }))
#
#     async def disconnect(self, code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     pass