from django.test import TestCase
from model_bakery import baker
from users.models import UserProfile
from django.contrib.auth.models import User


class UserProfileTest(TestCase):

    def setUp(self):
        self.user_profile = baker.make(
            UserProfile
        )

    def test_user_profile_instance(self):
        self.assertIsInstance(self.user_profile, UserProfile)

    def test_user_profile_user_relation(self):
        self.assertIsInstance(self.user_profile.user, User)
