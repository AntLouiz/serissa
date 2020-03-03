import os
import json
import uuid
import cv2
import numpy as np
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from serissa.settings import BASE_DIR
from users.models import Sra010
from users.api.serializers import UserModelSerializer


class UsersListAPIView(ListAPIView):

    model = Sra010
    serializer_class = UserModelSerializer

    def get_queryset(self, *args, **kwargs):
        return Sra010.objects.exclude(d_e_l_e_t_field='*')


class UsersCaptureAPIView(APIView):

    def post(self, request, **kwargs):
        matrice = request.data.get('matrice')
        image = request.data.get('image')

        if (matrice is None) or (image is None):
            return Response(status=HTTP_400_BAD_REQUEST)

        user = Sra010.objects.filter(
            ra_mat=matrice
        ).first()

        if user is None:
            return Response(
                data={'message': 'User not found'},
                status=HTTP_404_NOT_FOUND
            )

        filestr = image.read()
        image_array = np.fromstring(filestr, dtype=np.uint8)
        image = cv2.imdecode(image_array, -1)

        cascade_file = 'haarcascade_frontalface_alt.xml'
        cascades_dir = BASE_DIR.child('recognitor', 'cascades')
        cascade_path = f"{cascades_dir}/{cascade_file}"
        face_detector = cv2.CascadeClassifier(cascade_path)

        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
        except RuntimeError:
            return Response(
                data={'message': 'The image is not suported'},
                status=HTTP_400_BAD_REQUEST
            )

        if len(faces) != 1:
            return Response(
                data={
                    'message': 'The photo must contain a unique face \
                    of a person.'
                },
                status=HTTP_404_NOT_FOUND
            )

        x, y, w, h = faces[0]
        image = gray[y:y+h, x:x+w]

        captures_folder = BASE_DIR.child("media").child("captures")

        exists_folder = captures_folder.child(matrice).exists()

        file_id = str(uuid.uuid4())
        filename = f'{file_id}.jpg'

        if exists_folder:
            matrice_folder = captures_folder.child(matrice)
        else:
            matrice_folder = f"{captures_folder}/{matrice}"
            os.mkdir(matrice_folder)

        file_path = f"{matrice_folder}/{filename}"
        cv2.imwrite(file_path, image)

        return Response(status=HTTP_201_CREATED)
