# ipapp/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class IPUpdateConsumer(AsyncWebsocketConsumer):
    GROUP_NAME = "ip_updates"
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(self.GROUP_NAME, self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.GROUP_NAME, self.channel_name)

    async def ip_update(self, event):
        await self.send(text_data=json.dumps({
            "ip": event["ip"],
            "data": event["data"],
        }))

