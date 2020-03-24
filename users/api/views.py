import os
import uuid
import cv2
import numpy as np
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
)
from serissa.settings import BASE_DIR, CAPTURES_PER_USER_LIMIT
from users.models import UserProfile
from users.api.serializers import (
    UserModelSerializer,
    UsersCapturesSerializer,
    CapturesSerializer,
)


class ProfilesListAPIView(ListAPIView):

    model = UserProfile
    serializer_class = UserModelSerializer

    def get_queryset(self, *args, **kwargs):
        return UserProfile.objects.all()


class CapturesListAPIView(ListAPIView):
    model = UserProfile
    serializer_class = CapturesSerializer

    def get_queryset(self, *args, **kwargs):
        captures_folder = BASE_DIR.child("media").child("captures")
        captures_paths = captures_folder.listdir()
        matrices = []

        if len(captures_paths):
            users_matrices = [path.split('/')[-1] for path in captures_paths]
            for matrice in users_matrices:
                user_capture_path = BASE_DIR.child('media')\
                    .child('captures').child(matrice.rstrip())

                images = user_capture_path.listdir()

                if len(images):
                    matrices.append(matrice)

        users = UserProfile.objects.filter(
            matrice__in=matrices
        )

        return users


class UserCapturesRetrieveAPIView(RetrieveAPIView):

    model = UserProfile
    serializer_class = UsersCapturesSerializer
    lookup_field = 'matrice'

    def get_queryset(self, *args, **kwargs):
        matrice = self.kwargs.get('matrice')

        users = UserProfile.objects.filter(
            matrice=matrice
        )

        return users


class CaptureCreateAPIView(APIView):

    def post(self, request, **kwargs):
        matrice = request.data.get('matrice')
        images = request.FILES.getlist('images')

        if (matrice is None) or (images is None):
            return Response(
                status=HTTP_400_BAD_REQUEST,
                data={"message": "Must contain the matrice and images."}
            )

        user = UserProfile.objects.filter(
            matrice=matrice
        ).first()

        if user is None:
            return Response(
                status=HTTP_404_NOT_FOUND,
                data={'message': 'User not found'}
            )

        captures_folder = BASE_DIR.child("media").child("captures")
        exists_captures_folder = captures_folder.child(matrice).exists()

        if exists_captures_folder:
            matrice_folder = captures_folder.child(matrice)
            total_captures = len(matrice_folder.listdir())
            if total_captures >= CAPTURES_PER_USER_LIMIT:
                data = {
                    'message': 'Accepted only 15 photos peer users'
                }
                return Response(status=HTTP_403_FORBIDDEN, data=data)
        else:
            matrice_folder = f"{captures_folder}/{matrice}"
            os.mkdir(matrice_folder)
            total_captures = 0

        captures_diff_range = CAPTURES_PER_USER_LIMIT - total_captures
        rejected_images = [img.name for img in images[captures_diff_range:]]
        accepted_images = []

        images = images[:captures_diff_range]

        for image in images:
            filename = image.name
            filestr = image.read()
            image_array = np.fromstring(filestr, dtype=np.uint8)
            image_decoded = cv2.imdecode(image_array, -1)

            cascade_file = 'haarcascade_frontalface_alt.xml'
            cascades_dir = BASE_DIR.child('recognitor', 'cascades')
            cascade_path = f"{cascades_dir}/{cascade_file}"
            face_detector = cv2.CascadeClassifier(cascade_path)

            try:
                gray = cv2.cvtColor(image_decoded, cv2.COLOR_BGR2GRAY)
                faces = face_detector.detectMultiScale(gray, 1.3, 5)

                if len(faces):
                    accepted_images.append(filename)
                    x, y, w, h = faces[0]
                    image = gray[y:y+h, x:x+w]

                    file_id = str(uuid.uuid4())
                    filename = f'{file_id}.jpg'

                    file_path = f"{matrice_folder}/{filename}"
                    cv2.imwrite(file_path, image)
                else:
                    rejected_images.append(filename)

            except RuntimeError:
                rejected_images.append(image)

        if not len(accepted_images):
            return Response(
                status=HTTP_400_BAD_REQUEST,
                data={"message": "Only rejected images."}
            )

        data = {
            "accepteds": accepted_images,
            "rejecteds": rejected_images
        }

        return Response(status=HTTP_201_CREATED, data=data)


class UsersCaptureDeleteAPIView(DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        matrice = kwargs.get('matrice')
        image_key = kwargs.get('image_key')

        if (not matrice) or (not image_key):
            return Response(status=HTTP_400_BAD_REQUEST)

        captures_folder = BASE_DIR.child("media").child("captures")
        matrice_folder = captures_folder.child(matrice)
        exists_matrice_folder = matrice_folder.exists()

        image_file = f"{image_key}.jpg"

        user_image_path = matrice_folder.child(image_file)
        exists_user_image = user_image_path.exists()

        if (not exists_matrice_folder) or (not exists_user_image):
            message = 'Matrice and image key must exists on the server'
            return Response(
                status=HTTP_404_NOT_FOUND,
                data={'message': message}
            )

        try:
            user_image_path.remove()
        except PermissionError:
            message = 'Permission denied to remove that file'
            return Response(
                status=HTTP_404_NOT_FOUND,
                data={'message': message}
            )

        return Response(
            status=HTTP_200_OK,
            data={
                'message': 'Capture deleted successfully',
                'image_key': image_key
            }
        )
