from django.test import TestCase
from model_bakery import baker
from users.models import UserProfile
from users.api.serializers import CapturesSerializer


class TestCapturesSerializer(TestCase):

    def setUp(self):
        user = baker.make(
            UserProfile
        )

        self.serializer = CapturesSerializer(user)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        expected_fields = [
            'name',
            'matrice',
            'image_path'
        ]

        self.assertEqual(
            set(data.keys()),
            set(expected_fields)
        )
