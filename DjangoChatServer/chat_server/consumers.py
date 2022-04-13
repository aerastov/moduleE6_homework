import json
from .models import UserProfile, Room
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


def userlist():
    objects = UserProfile.objects.filter()
    list = {'UserList': 'UserList'}
    for object in objects:
        list[object.id] = object.name
    return list

def roomlist():
    objects = Room.objects.filter()
    list = {'RoomList': 'RoomList'}
    for object in objects:
        list[object.id] = object.name
    return list


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(json.dumps({'message': 'соединение установлено'}))
        async_to_sync(self.channel_layer.group_add)("all_instructions", self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("all_instructions", self.channel_name)

    def all_user(self, text_data=None):
        message = text_data
        print('order for all users:', message)
        if message['order'] == "send_list_users":
            self.send(json.dumps(userlist()))
            print('новый список юзеров отправлен всем клиентам')
        if message['order'] == "send_list_rooms":
            self.send(json.dumps(roomlist()))
            print('новый список комнат отправлен всем клиентам')

    def receive(self, text_data=None, bytes_data=None):
        message = json.loads(text_data)
        print('receive path:', self.scope["path"])
        print('receive message:', message)

        if 'load' in message:
            if message['load'] == "users":
                self.send(json.dumps(userlist()))
                print('список юзеров отправлен клиенту')
            if message['load'] == 'rooms':
                self.send(json.dumps(roomlist()))
                print('список комнат отправлен клиенту')

        if 'create_user' in message:
            name = message['create_user']
            if not UserProfile.objects.filter(name=name).exists():
                user = UserProfile(name=name)
                user.save()
                print('новый юзер', name, "создан")
                async_to_sync(self.channel_layer.group_send)("all_instructions", {"type": "all_user", "order": "send_list_users"})
            else:
                self.send(json.dumps({'message': 'Такой юзер уже существует'}))
                print('такой юзер уже существует')

        if 'create_room' in message:
            name = message['create_room']
            if not Room.objects.filter(name=name).exists():
                room = Room(name=name)
                room.save()
                print('новая комната', name, "создана")
                async_to_sync(self.channel_layer.group_send)("all_instructions", {"type": "all_user", "order": "send_list_rooms"})
            else:
                self.send(json.dumps({'message': 'Такая комната уже существует'}))
                print('такая комната уже существует')

        if 'delete_user' in message:
            id = message['delete_user']
            user = UserProfile.objects.get(id=id)
            user.delete()
            print('юзер ID', id, "удален")
            async_to_sync(self.channel_layer.group_send)("all_instructions", {"type": "all_user", "order": "send_list_users"})

        if 'delete_room' in message:
            id = message['delete_room']
            room = Room.objects.get(id=id)
            room.delete()
            print('комната ID', id, "удалена")
            async_to_sync(self.channel_layer.group_send)("all_instructions", {"type": "all_user", "order": "send_list_rooms"})

        if 'order' in message:
            if message['order'] == 'changeUserName':
                id = message['id']
                name = message['name']
                if not UserProfile.objects.filter(name=name).exists():
                    user = UserProfile.objects.get(id=id)
                    user.name = name
                    user.save()
                    print('имя юзера ID:', id, 'изменено на:', name)
                    async_to_sync(self.channel_layer.group_send)("all_instructions", {"type": "all_user", "order": "send_list_users"})
                else:
                    self.send(json.dumps({'message': 'Такой юзер уже существует'}))
                    print('такой юзер уже существует')

            if message['order'] == 'changeRoomName':
                id = message['id']
                name = message['name']
                if not Room.objects.filter(name=name).exists():
                    room = Room.objects.get(id=id)
                    room.name = name
                    room.save()
                    print('имя комнаты ID:', id, 'изменено на:', name)
                    async_to_sync(self.channel_layer.group_send)("all_instructions", {"type": "all_user", "order": "send_list_rooms"})
                else:
                    self.send(json.dumps({'message': 'Такая комната уже существует'}))
                    print('такая комната уже существует')


class WSChat(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(json.dumps({'message': 'соединение c комнатой установлено'}))
        async_to_sync(self.channel_layer.group_add)("all_chat", self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("all_chat", self.channel_name)

    def all_room(self, text_data=None):
        message = text_data
        print('order for all rooms:', message)

    #     # Создаём сообщение в БД
    #     Message.objects.create(text=message)

