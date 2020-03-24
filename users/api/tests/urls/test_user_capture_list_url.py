from django.test import TestCase
from django.urls import reverse, resolve
from users.api.views import CapturesListAPIView


class TestUserCaptureListUrl(TestCase):

    def setUp(self):
        self.url = '/users/api/captures'

    def test_reverse_user_capture_list_url(self):
        user_capture_list_url = reverse(
            'users:api:captures'
        )

        self.assertEqual(
            user_capture_list_url,
            self.url
        )

    def test_resolve_user_capture_list_url(self):
        found = resolve(self.url)

        self.assertEqual(
            found.func.__name__,
            CapturesListAPIView.as_view().__name__
        )
