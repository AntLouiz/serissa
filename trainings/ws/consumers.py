import json
from channels.generic.websocket import AsyncWebsocketConsumer


class TrainingConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        channel_key = str(self.scope['url_route']['kwargs'].get('channel_key'))

        if channel_key is None or channel_key not in ['face_recognition']:
            await self.disconnect()

        await self.channel_layer.group_add(
            channel_key,
            self.channel_name
        )
        print(f"Connection opened on group channel: {channel_key}.")
        await self.accept()

    async def send_progress(self, event):
        progress = event['message']
        await self.send(json.dumps(progress))

    async def disconnect(self, code):
        self.close()
