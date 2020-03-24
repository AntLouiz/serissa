from django.test import TestCase
from django.urls import reverse, resolve
from users.api.views import CaptureDeleteAPIView


class TestDeleteCaptureUrl(TestCase):

    def setUp(self):
        self.matrice = '11111'
        self.key = 'someimagekey'
        self.url = f"/users/api/{self.matrice}/capture/{self.key}/delete"

    def test_reverse_capture_delete_url(self):
        capture_delete_url = reverse(
            'users:api:delete-capture',
            kwargs={
                'matrice': self.matrice,
                'capture_key': self.key
            }
        )

        self.assertEqual(
            capture_delete_url,
            self.url
        )

    def test_resolve_capture_delete_url(self):
        found = resolve(self.url)

        self.assertEqual(
            found.func.__name__,
            CaptureDeleteAPIView.as_view().__name__
        )
