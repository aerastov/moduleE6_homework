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
        async_to_sync(self.channel_layer.group_add)("all", self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("all", self.channel_name)

    def all_room(self, text_data=None, bytes_data=None):
        message = text_data
        print('order for all rooms:', message)
        if message['order'] == "send_list_users":
            self.send(json.dumps(userlist()))
            print('новый список юзеров отправлен всем клиентам')

    def receive(self, text_data=None, bytes_data=None):
        message = json.loads(text_data)
        print('receive path:', self.scope["path"])
        print('receive message:', message)

        if 'load' in message:
            if message['load'] == "users":
                self.send(json.dumps(userlist()))
                print('список юзеров отправлен клиенту')

        if 'create_user' in message:
            name = message['create_user']
            if not UserProfile.objects.filter(name=name).exists():
                user = UserProfile(name=name)
                user.save()
                print('новый юзер', name, "создан")
                async_to_sync(self.channel_layer.group_send)("all", {"type": "all_room", "order": "send_list_users"})
            else:
                self.send(json.dumps({'message': 'Такой юзер уже существует'}))
                print('такой юзер уже существует')
        if 'delete_user' in message:
            id = message['delete_user']
            user = UserProfile.objects.get(id=id)
            user.delete()
            print('юзер', "удален")
            async_to_sync(self.channel_layer.group_send)("all", {"type": "all_room", "order": "send_list_users"})



    #     # Создаём сообщение в БД
    #     Message.objects.create(text=message)

