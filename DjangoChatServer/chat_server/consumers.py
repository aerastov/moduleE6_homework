import json
from .models import UserProfile
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


def userlist():
    objects = (UserProfile.objects.filter())
    list = {'UserList': 'UserList'}
    for object in objects:
        list[object.id] = object.name
    return list


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(json.dumps({'message': 'соединение установлено'}))

    def receive(self, text_data=None, bytes_data=None):
        message = json.loads(text_data)
        print('receive path:', self.scope["path"])
        print('receive message:', message)
        if 'load' in message:
            if message['load'] == "users":
                self.send(json.dumps(userlist()))
                print('список юзеров отправлен ws клиенту')
        if 'create_user' in message:
            name = message['create_user']
            if not UserProfile.objects.filter(name=name).exists():
                user = UserProfile(name=name)
                user.save()
                print('новый юзер', name, "создан")
                self.send(json.dumps(userlist()))
                print('новый список юзеров отправлен ws клиенту')
            else:
                self.send(json.dumps({'message': 'Такой юзер уже существует'}))
                print('такой юзер уже существует')
        if 'delete_user' in message:
            id = message['delete_user']
            user = UserProfile.objects.get(id=id)
            user.delete()
            print('юзер', "удален")
            self.send(json.dumps(userlist()))
            print('новый список юзеров отправлен ws клиенту')






    # class ChatConsumer(AsyncWebsocketConsumer):
    #     # Принимам сообщение от пользователя
    #     async def receive(self, text_data=None, bytes_data=None):
    # # Добавляем сообщение в БД
    # await self.new_message(message=message)

    # # Отправляем сообщение
    # await self.channel_layer.group_send(
    #     self.room_group_name,
    #     {
    #         'type': 'chat_message',
    #         'message': message,
    #     }
    # )

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