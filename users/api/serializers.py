import os.path
from rest_framework.serializers import (
    Serializer,
    SerializerMethodField,
    ModelSerializer,
    IntegerField,
    CharField,
)
from serissa.settings import BASE_DIR, MEDIA_URL
from users.models import UserProfile


class UserModelSerializer(ModelSerializer):
    code = IntegerField(source="pk")
    name = CharField(source="user.first_name")
    matrice = CharField()

    class Meta:
        model = UserProfile
        fields = ['code', 'name', 'matrice']


class CapturesSerializer(Serializer):
    matrice = CharField()
    name = CharField(source='user.first_name')
    image_path = SerializerMethodField()

    def get_image_path(self, obj):
        user_capture_path = BASE_DIR.child('media')\
            .child('captures').child(obj.matrice)

        images = user_capture_path.listdir()

        if not len(images):
            return None

        first_image_path = images[0]

        return os.path.join(
            MEDIA_URL,
            'captures',
            obj.matrice,
            first_image_path.name
        )


class UsersCapturesSerializer(CapturesSerializer):
    image_path = None
    captures_paths = SerializerMethodField()

    def get_captures_paths(self, obj):
        user_capture_path = BASE_DIR.child('media')\
            .child('captures').child(obj.matrice)

        images_paths = user_capture_path.listdir()
        user_captures = []

        for path in images_paths:
            user_captures.append(
                os.path.join(
                    'media',
                    'captures',
                    obj.matrice,
                    path.name
                )
            )

        return user_captures
