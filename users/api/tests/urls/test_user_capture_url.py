from django.test import TestCase
from django.urls import reverse, resolve
from users.api.views import UsersCaptureAPIView


class TestUserCaptureUrl(TestCase):
    def setUp(self):
        self.url = '/users/api/capture'

    def test_reverse_user_capture_api_url(self):
        user_capture_url = reverse(
            'users:api:create-capture'
        )

        self.assertEqual(
            user_capture_url,
            self.url
        )

    def test_resolve_user_capture_api_url(self):
        found = resolve(self.url)

        self.assertEqual(
            found.func.__name__,
            UsersCaptureAPIView.as_view().__name__
        )
