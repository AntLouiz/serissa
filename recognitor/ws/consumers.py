import json
from channels.generic.websocket import AsyncWebsocketConsumer


class RecognitorConsumer(AsyncWebsocketConsumer):

    def get_fact_code(self):
        kwargs = self.scope['url_route']['kwargs']

        print(kwargs)

        return False

    async def connect(self):
        await self.accept()

    async def send_message(self):
        await self.send(json.dumps({"message": "Hello"}))

    async def disconnect(self, code):
        self.close()
