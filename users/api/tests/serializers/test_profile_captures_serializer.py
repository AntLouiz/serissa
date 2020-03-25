from django.test import TestCase
from model_bakery import baker
from users.models import UserProfile
from users.api.serializers import UserProfileCapturesSerializer


class TestUserProfileCapturesSerializer(TestCase):

    def setUp(self):
        user = baker.make(UserProfile)
        self.serializer = UserProfileCapturesSerializer(user)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        expecteds_fields = ['image_path', 'captures_paths']

        self.assertEqual(
            set(data.keys()),
            set(expecteds_fields)
        )
