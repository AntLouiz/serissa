from django.test import TestCase
from model_bakery import baker
from captures.models import CapturePack, FaceImageCapture
from captures.api.serializers import FaceImageCaptureSerializer


class TestFaceImageCaptureSerializer(TestCase):

    def setUp(self):
        self.pack = baker.make(
            CapturePack
        )

        capture = baker.make(
            FaceImageCapture,
            pack=self.pack
        )

        self.serializer = FaceImageCaptureSerializer(
            capture
        )

    def test_contains_expected_fields(self):
        data = self.serializer.data

        expected_fields = [
            'pack',
            'path',
            'created_at'
        ]

        self.assertEqual(
            set(data.keys()),
            set(expected_fields)
        )
