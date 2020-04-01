from django.test import TestCase
from captures.models import CapturePack


class TestCapturePackModel(TestCase):

    def setUp(self):
        self.capture_pack = CapturePack()

    def test_capture_pack_instance(self):
        self.assertIsInstance(
            self.capture_pack,
            CapturePack
        )

    def test_capture_pack_fields(self):
        capture_pack_fields = [f.name for f in self.capture_pack._meta.local_fields]

        expected_fields = [
            'id',
            'profile',
            'created_at',
            'updated_at',
            'is_active'
        ]

        self.assertEqual(
            set(capture_pack_fields),
            set(expected_fields)
        )
