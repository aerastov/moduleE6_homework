from django.urls import path
from .views import ApiUsers, ApiRooms
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .consumers import userlist

router = DefaultRouter()
router.register('rooms', ApiRooms)
router.register('users', ApiUsers)

urlpatterns = [
    path('api/', include(router.urls)),
]

