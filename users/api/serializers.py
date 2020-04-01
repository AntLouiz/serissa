from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
)
from users.models import UserProfile


class UserProfileSerializer(ModelSerializer):
    code = IntegerField(source="pk")
    name = CharField(source="user.first_name")
    matrice = CharField()

    class Meta:
        model = UserProfile
        fields = ['code', 'name', 'matrice']
