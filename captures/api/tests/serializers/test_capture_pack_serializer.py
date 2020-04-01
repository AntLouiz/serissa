from django.test import TestCase
from model_bakery import baker
from captures.models import CapturePack, FaceImageCapture
from captures.api.serializers import CapturePackSerializer


class TestCapturePackSerializer(TestCase):

    def setUp(self):
        self.pack = baker.make(
            CapturePack
        )

        self.captures = baker.make(
            FaceImageCapture,
            pack=self.pack,
            _quantity=5
        )

        self.serialized_data = CapturePackSerializer(
            instance=self.pack
        ).data

    def test_contains_expected_fields(self):
        data = self.serialized_data

        expected_fields = [
            'id',
            'profile',
            'created_at',
            'updated_at',
            'is_active',
            'captures'
        ]

        self.assertEqual(
            set(data.keys()),
            set(expected_fields)
        )
