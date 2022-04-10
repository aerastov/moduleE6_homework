from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField


class Room(models.Model):
    name = models.CharField(max_length=256, unique=True)

class UserProfile(models.Model):
    name = models.CharField(max_length=256, unique=True)
    avatar = ThumbnailerImageField(resize_source={'size': (200, 200), 'crop': 'smart'}, upload_to='djangochatserver', default='djangochatserver/default.jpg')
    avatar_small = ThumbnailerImageField(resize_source={'size': (30, 30), 'crop': 'smart'}, upload_to='djangochatserver', default='djangochatserver/default_small.jpg')
    room = models.OneToOneField(Room, on_delete=models.SET_NULL, null=True)
    # online = models.BooleanField(default=False)


class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    text = models.CharField(max_length=255)

