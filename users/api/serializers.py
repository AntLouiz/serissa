from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
)
from users.models import Sra010


class UserModelSerializer(ModelSerializer):
    code = IntegerField(source="r_e_c_n_o_field")
    name = CharField(source="ra_nome")
    matrice = CharField(source="ra_mat")

    class Meta:
        model = Sra010
        fields = ['code', 'name', 'matrice']
