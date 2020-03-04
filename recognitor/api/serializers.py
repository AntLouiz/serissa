import os.path
from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    IntegerField,
    CharField,
    SerializerMethodField
)
from users.models import Zq0010, Zq1010, Sra010
from serissa.settings import BASE_DIR, MEDIA_URL


class AttemptsModelSerializer(ModelSerializer):
    code = IntegerField(source="r_e_c_n_o_field")
    confidence = IntegerField(source="zq1_confid")
    date = CharField(source="zq1_dt")
    recognized = CharField(source="zq1_rec")
    algorithm = SerializerMethodField()
    image_path = SerializerMethodField()
    matrice = SerializerMethodField()
    name = SerializerMethodField()

    class Meta:
        model = Zq1010
        fields = [
            'code',
            'name',
            'matrice',
            'algorithm',
            'confidence',
            'recognized',
            'date',
            'image_path',
        ]

    def get_algorithm(self, obj):
        return obj.zq1_alg.rstrip()

    def get_matrice(self, obj):
        matrice = Zq0010.objects.get(zq0_cod=obj.zq1_fcod).zq0_usuario
        return matrice.rstrip()

    def get_image_path(self, obj):
        image_path = Zq0010.objects.get(zq0_cod=obj.zq1_fcod).zq0_img
        return image_path.rstrip()

    def get_name(self, obj):
        name = 'unknown'
        matrice = Zq0010.objects.get(zq0_cod=obj.zq1_fcod).zq0_usuario

        if matrice != 'unknown':
            user = Sra010.objects.filter(
                ra_mat=matrice
            ).first()

            if user:
                name = user.ra_nome

        return name.rstrip()


class CapturesSerializer(Serializer):
    matrice = CharField(max_length=100, source='ra_mat')
    name = CharField(max_length=200, source='ra_nome')
    image_path = SerializerMethodField()

    def get_image_path(self, obj):
        user_capture_path = BASE_DIR.child('media')\
            .child('captures').child(obj.ra_mat.rstrip())

        first_image_path = user_capture_path.listdir()[0]

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
