import json
from channels.generic.websocket import AsyncWebsocketConsumer


class TrainingProgressConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add(
            'progress',
            self.channel_name
        )
        await self.accept()

    async def send_progress(self, event):
        progress = event['message']
        await self.send(json.dumps(progress))

    async def disconnect(self, code):
        self.close()
