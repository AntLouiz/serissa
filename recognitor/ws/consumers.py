import os.path
import json
import base64
import cv2
import numpy as np
from datetime import datetime
from PIL import Image
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from recognitor.algorithms.faces_recognition import recognize_face
from users.models import Zq0010, Zq1010
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
        self, filial, alg,
        confidence, date, reconized,
        matrice, image_array
    ):
        last_attempt = Zq1010.objects.all().last()

        if last_attempt:
            code = int(Zq1010.objects.all().last().zq1_cod) + 1
        else:
            code = 1

        last_face_path = Zq0010.objects.all().last()

        if last_face_path:
            path_code = int(last_face_path.zq0_cod) + 1
        else:
            path_code = 1

        filename = "{}_{}_{}.png".format(
            path_code,
            matrice,
            date
        )

        attempt_image_path = os.path.join(
            'media',
            'attempts',
            filename
        )

        face_path = Zq0010.objects.create(
            zq0_filial='01',
            zq0_cod=str(path_code),
            zq0_usuario=matrice,
            zq0_img=attempt_image_path,
            r_e_c_n_o_field=path_code,
            d_e_l_e_t_field=' ',
            r_e_c_d_e_l_field=0
        )

        Zq1010.objects.create(
            zq1_filial=filial,
            zq1_cod=str(code),
            zq1_alg=alg,
            zq1_confid=confidence,
            zq1_dt=date,
            zq1_rec=reconized,
            zq1_fcod=face_path.zq0_cod,
            r_e_c_n_o_field=path_code,
            d_e_l_e_t_field=' ',
            r_e_c_d_e_l_field=0
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

        now = datetime.now().strftime('%Y%m%d')
        reconized = 'N'

        if matrice != 'unknown':
            reconized = 'S'

        await self.create_recognition_attempt(
            '01',
            'face_recognition',
            confidence,
            now,
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
