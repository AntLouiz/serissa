from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
    SerializerMethodField
)
from users.models import Zq0010, Zq1010, Sra010


class AttemptsModelSerializer(ModelSerializer):
    code = IntegerField(source="r_e_c_n_o_field")
    confidence = IntegerField(source="zq1_confid")
    date = CharField(source="zq1_dt")
    recognized = CharField(source="zq1_rec")
    algorithm = CharField(source="zq1_alg")
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

    def get_matrice(self, obj):
        return Zq0010.objects.get(zq0_cod=obj.zq1_fcod).zq0_usuario

    def get_image_path(self, obj):
        return Zq0010.objects.get(zq0_cod=obj.zq1_fcod).zq0_img

    def get_name(self, obj):
        name = 'unknown'
        matrice = Zq0010.objects.get(zq0_cod=obj.zq1_fcod).zq0_usuario

        if matrice != 'unknown':
            user = Sra010.objects.filter(
                ra_mat=matrice
            ).first()

            if user:
                name = user.ra_nome

        return name
