import os.path
import json
import uuid
import base64
import cv2
import numpy as np
from PIL import Image
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from recognitor.algorithms.faces_recognition import recognize_face
from recognitor.models import FaceImage, RecognitionAttempt
from users.models import UserProfile
from serissa.settings import BASE_DIR


class RecognitorConsumer(AsyncWebsocketConsumer):

    def decode_client_message_to_image(self, message):
        message = json.loads(message)
        origin = message['origin']
        encoded_img = message['image']

        original_image = base64.b64decode(encoded_img)
        client_data = np.frombuffer(original_image, dtype=np.uint8)
        image = cv2.imdecode(client_data, -1)
        return origin, image

    @database_sync_to_async
    def create_recognition_attempt(
        self, algorithm, confidence,
        origin, reconized,
        matrice, image_array
    ):

        file_uuid = uuid.uuid4()
        filename = "{}.jpg".format(
            str(file_uuid)
        )

        attempt_image_path = os.path.join(
            'media',
            'attempts',
            filename
        )

        profile = UserProfile.objects.filter(matrice=matrice).first()

        face_path = FaceImage.objects.create(
            user=profile,
            path=attempt_image_path
        )

        RecognitionAttempt.objects.create(
            algorithm=algorithm,
            confidence=confidence,
            origin=origin,
            recognized=reconized,
            face_image=face_path
        )

        im = Image.fromarray(image_array)
        image_path = os.path.join(BASE_DIR, attempt_image_path)
        im.save(image_path)

    async def connect(self):
        print("Connection openned.")
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        origin, image_array = self.decode_client_message_to_image(text_data)

        # On this point, the system need to recognize the image to each
        # algorithm in parallel

        matrice, confidence = recognize_face(image_array)

        if matrice is None:
            matrice = 'unknown'

        reconized = False

        if matrice != 'unknown':
            reconized = True

        await self.create_recognition_attempt(
            'face_recognition',
            confidence,
            origin,
            reconized,
            matrice,
            image_array
        )

        data = {
            'matrice': matrice,
            'confidence': confidence
        }

        await self.send(json.dumps(data))

    async def disconnect(self, code):
        self.close()
