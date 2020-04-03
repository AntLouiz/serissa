from unittest import mock
from django.test import TestCase
from model_bakery import baker
from captures.models import CapturePack, FaceImageCapture
from captures.api.serializers import CapturePackSerializer


class TestCapturePackSerializer(TestCase):

    @mock.patch('captures.utils.os.mkdir')
    def setUp(self, os_mkdir_mock):
        os_mkdir_mock.return_value = None

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

    @mock.patch('captures.utils.os.mkdir')
    def test_contains_expected_fields(self, os_mkdir_mock):
        os_mkdir_mock.return_value = None
        data = self.serialized_data

        expected_fields = [
            'id',
            'profile',
            'path',
            'created_at',
            'updated_at',
            'is_active',
            'captures'
        ]

        self.assertEqual(
            set(data.keys()),
            set(expected_fields)
        )
