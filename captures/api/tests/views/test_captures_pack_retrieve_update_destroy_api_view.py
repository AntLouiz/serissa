from unittest import mock
from rest_framework.test import APITestCase
from django.urls import reverse
from model_bakery import baker
from users.models import UserProfile
from captures.models import CapturePack, FaceImageCapture
from captures.api.serializers import CapturePackSerializer


class TestCapturesPackRetrieveUpdateDestroyAPIView(APITestCase):

    @mock.patch('captures.utils.os.mkdir')
    def setUp(self, os_mkdir_mock):
        os_mkdir_mock.return_value = None

        self.capture = baker.make(
            CapturePack
        )

        self.reversed_url = reverse(
            'captures:api:retrieve-update-destroy-captures-pack',
            kwargs={
                'pk': self.capture.pk
            }
        )

        self.serialized_data = CapturePackSerializer(
            self.capture
        ).data

    def test_retrieve_response_object_bundle(self):
        response = self.client.get(self.reversed_url)

        self.assertEqual(response.status_code, 200)

        data = response.data

        self.assertEqual(
            data,
            self.serialized_data
        )

    def test_update_response_object_request(self):
        pass
