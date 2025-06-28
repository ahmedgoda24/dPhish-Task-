# ipapp/routing.py
from django.urls import re_path
from .consumers import IPUpdateConsumer

websocket_urlpatterns = [
    re_path(r'ws/ip-updates/$', IPUpdateConsumer.as_asgi()),
]
