from django.test import TestCase
from model_bakery import baker
from users.models import UserProfile
from users.api.serializers import UserProfileSerializer


class TestProfileSerializer(TestCase):

    def setUp(self):
        user_profile = baker.make(UserProfile)
        self.serializer = UserProfileSerializer(user_profile)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        expected_fields = ['code', 'name', 'matrice']

        self.assertEqual(
            set(data.keys()),
            set(expected_fields)
        )
