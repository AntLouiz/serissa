from django.test import TestCase
from model_bakery import baker
from users.models import UserProfile


class ModelUserProfileTest(TestCase):

    def setUp(self):
        self.user_profile = baker.make(
            UserProfile
        )

    def test_user_profile_instance(self):
        self.assertIsInstance(self.user_profile, UserProfile)

    def test_user_profile_fields(self):
        capture_fields = [f.name for f in self.user_profile._meta.local_fields]
        expected_fields = ['id', 'matrice', 'user']

        self.assertEqual(
            capture_fields,
            expected_fields
        )
