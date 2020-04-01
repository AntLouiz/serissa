from django.test import TestCase
from captures.models import BaseFaceImage, FaceImageAttempt


class TestFaceImageAttemptModel(TestCase):

    def setUp(self):
        self.face_attempt = FaceImageAttempt()

    def test_face_image_capture_instance(self):
        self.assertIn(BaseFaceImage, FaceImageAttempt.__mro__)
        self.assertIsInstance(self.face_attempt, FaceImageAttempt)

    def test_face_image_fields(self):
        capture_fields = [f.name for f in self.face_attempt._meta.local_fields]
        expected_fields = [
            'id',
            'path',
            'pack',
            'created_at',
            'algorithm',
            'confidence',
            'date',
            'recognized',
            'origin',
            'is_active'
        ]

        self.assertEqual(
            set(capture_fields),
            set(expected_fields)
        )
