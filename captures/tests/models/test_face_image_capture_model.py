from django.test import TestCase
from captures.models import BaseFaceImage, FaceImageCapture


class TestFaceImageCaptureModel(TestCase):

    def setUp(self):
        self.face_capture = FaceImageCapture()

    def test_face_image_capture_instance(self):
        self.assertIn(BaseFaceImage, FaceImageCapture.__mro__)
        self.assertIsInstance(self.face_capture, FaceImageCapture)

    def test_face_image_fields(self):
        capture_fields = [f.name for f in self.face_capture._meta.local_fields]
        expected_fields = ['id', 'path', 'pack', 'created_at', 'is_active']

        self.assertEqual(
            set(capture_fields),
            set(expected_fields)
        )
