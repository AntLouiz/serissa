from django.test import TestCase
from django.urls import reverse, resolve
from model_bakery import baker
from captures.models import CapturePack
from captures.api.views import CapturesPackRetrieveUpdateDestroyAPIView


class TestCapturesPackRetrieveUpdateDestroyUrl(TestCase):

    def setUp(self):
        self.capture = baker.make(
            CapturePack
        )
        self.reversed_url = reverse(
            'captures:api:retrieve-update-destroy-captures-pack',
            kwargs={
                'pk': self.capture.pk
            }
        )

    def test_reverse_user_capture_url(self):
        self.assertEqual(
            f'/captures/{self.capture.pk}',
            self.reversed_url
        )

    def test_resolve_user_capture_url(self):
        found = resolve(self.reversed_url)

        self.assertEqual(
            found.func.__name__,
            CapturesPackRetrieveUpdateDestroyAPIView.as_view().__name__
        )
