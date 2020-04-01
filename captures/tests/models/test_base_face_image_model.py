from django.test import TestCase
from captures.models import BaseFaceImage


class TestBaseFaceImageModel(TestCase):

    def setUp(self):
        self.abstract_class = BaseFaceImage

    def test_is_abstract(self):
        self.assertTrue(self.abstract_class._meta.abstract)

    def test_base_face_image_expected_fields(self):
        capture_fields = [f.name for f in self.abstract_class._meta.local_fields]
        expected_fields = ['path', 'created_at', 'is_active']

        self.assertEqual(
            set(capture_fields),
            set(expected_fields)
        )
