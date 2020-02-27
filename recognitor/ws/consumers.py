import json
import base64
import cv2
import numpy as np
from channels.generic.websocket import AsyncWebsocketConsumer
from recognitor.algorithms.faces_recognition import recognize_face


class RecognitorConsumer(AsyncWebsocketConsumer):

    def decode_client_message_to_image(self, message):
        message = json.loads(message)
        origin = message['origin']
        encoded_img = message['image']

        original_image = base64.b64decode(encoded_img)
        client_data = np.frombuffer(original_image, dtype=np.uint8)
        image = cv2.imdecode(client_data, -1)
        return origin, image

    async def connect(self):
        print("Connection openned.")
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        origin, image = self.decode_client_message_to_image(text_data)

        # On this point, the system need to recognize the image to each
        # algorithm in parallel

        matrice, confidence = recognize_face(image)
        data = {
            'matrice': matrice,
            'confidence': confidence
        }
        print(data)

        self.send(json.dumps(data))

    async def disconnect(self, code):
        self.close()
