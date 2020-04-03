from django.test import TestCase
from django.urls import reverse, resolve
from captures.api.views import CapturesPackListCreateAPIView


class TestCapturesPackListCreateAPIUrl(TestCase):

    def setUp(self):
        self.reversed_url = reverse(
            'captures:api:list-create-captures-pack'
        )

    def test_reverse_user_capture_url(self):
        self.assertEqual(
            '/captures/',
            self.reversed_url
        )

    def test_resolve_user_capture_url(self):
        found = resolve(self.reversed_url)

        self.assertEqual(
            found.func.__name__,
            CapturesPackListCreateAPIView.as_view().__name__
        )