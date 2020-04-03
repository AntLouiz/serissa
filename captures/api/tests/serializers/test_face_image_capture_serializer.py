from unittest import mock
from django.test import TestCase
from model_bakery import baker
from captures.models import CapturePack, FaceImageCapture
from captures.api.serializers import FaceImageCaptureSerializer


class TestFaceImageCaptureSerializer(TestCase):

    @mock.patch('captures.utils.os.mkdir')
    def setUp(self, os_mkdir_mock):
        os_mkdir_mock.return_value = None

        self.pack = baker.make(
            CapturePack
        )

        capture = baker.make(
            FaceImageCapture,
            pack=self.pack
        )

        self.serializer = FaceImageCaptureSerializer(
            capture
        ).data

    def test_contains_expected_fields(self):
        data = self.serializer

        expected_fields = [
            'pack',
            'path',
            'created_at'
        ]

        self.assertEqual(
            set(data.keys()),
            set(expected_fields)
        )
