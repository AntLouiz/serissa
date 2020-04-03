from rest_framework.serializers import ModelSerializer
from captures.models import CapturePack, FaceImageCapture


class FaceImageCaptureSerializer(ModelSerializer):

    class Meta:
        model = FaceImageCapture
        fields = ['pack', 'path', 'created_at']


class CapturePackSerializer(ModelSerializer):

    captures = FaceImageCaptureSerializer(many=True, read_only=True)

    class Meta:
        model = CapturePack
        fields = [
            'id',
            'profile',
            'path',
            'created_at',
            'updated_at',
            'is_active',
            'captures'
        ]
