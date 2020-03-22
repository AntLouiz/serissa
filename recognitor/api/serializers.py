from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    FloatField,
    DateTimeField,
    CharField,
    SerializerMethodField
)
from recognitor.models import FaceImage, RecognitionAttempt
from users.models import UserProfile


class AttemptsModelSerializer(ModelSerializer):
    code = IntegerField(source="pk")
    confidence = FloatField()
    created_at = DateTimeField()
    origin = CharField()
    recognized = CharField()
    algorithm = SerializerMethodField()
    image_path = SerializerMethodField()
    matrice = SerializerMethodField()
    name = SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            'code',
            'name',
            'matrice',
            'algorithm',
            'confidence',
            'recognized',
            'date',
            'hour',
            'origin',
            'image_path',
        ]

    def get_image_path(self, obj):
        image_path = FaceImage.objects.get(pk=obj.face_image).path
        return image_path

    def get_name(self, obj):
        return obj.user.first_name
