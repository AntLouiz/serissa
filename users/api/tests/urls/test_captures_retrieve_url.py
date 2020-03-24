from django.test import TestCase
from django.urls import reverse, resolve
from users.api.views import CapturesRetrieveAPIView


class TestCapturesRetrieveUrl(TestCase):

    def setUp(self):
        self.matrice = '111111'
        self.url = f"/users/api/{self.matrice}/captures"

    def test_reverse_captures_retrieve_url(self):
        captures_user_list_url = reverse(
            'users:api:retrieve-captures',
            kwargs={'matrice': self.matrice}
        )

        self.assertEqual(
            captures_user_list_url,
            self.url
        )

    def test_resolve_captures_retrieve_url(self):
        found = resolve(
            self.url
        )

        self.assertEqual(
            found.func.__name__,
            CapturesRetrieveAPIView.as_view().__name__
        )
