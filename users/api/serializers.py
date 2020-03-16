import os.path
from rest_framework.serializers import (
    Serializer,
    SerializerMethodField,
    ModelSerializer,
    IntegerField,
    CharField,
)
from serissa.settings import BASE_DIR, MEDIA_URL
from users.models import Sra010


class UserModelSerializer(ModelSerializer):
    code = IntegerField(source="r_e_c_n_o_field")
    name = CharField(source="ra_nome")
    matrice = CharField(source="ra_mat")

    class Meta:
        model = Sra010
        fields = ['code', 'name', 'matrice']


class CapturesSerializer(Serializer):
    matrice = CharField(max_length=100, source='ra_mat')
    name = CharField(max_length=200, source='ra_nome')
    image_path = SerializerMethodField()

    def get_image_path(self, obj):
        user_capture_path = BASE_DIR.child('media')\
            .child('captures').child(obj.ra_mat.rstrip())

        images = user_capture_path.listdir()

        if not len(images):
            return None

        first_image_path = images[0]

        return os.path.join(
            MEDIA_URL,
            'captures',
            obj.ra_mat,
            first_image_path.name
        )


class UsersCapturesSerializer(CapturesSerializer):
    image_path = None
    captures_paths = SerializerMethodField()

    def get_captures_paths(self, obj):
        user_capture_path = BASE_DIR.child('media')\
            .child('captures').child(obj.ra_mat.rstrip())

        images_paths = user_capture_path.listdir()
        user_captures = []

        for path in images_paths:
            user_captures.append(
                os.path.join(
                    'media',
                    'captures',
                    obj.ra_mat,
                    path.name
                )
            )

        return user_captures
