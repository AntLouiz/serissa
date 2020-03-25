from unittest.mock import Mock
from uuid import uuid4
from collections import OrderedDict
from django.urls import reverse
from rest_framework.test import APITestCase
from model_bakery import baker
from users.models import UserProfile


class TestCapturesListAPIView(APITestCase):

    def setUp(self):
        self.url = reverse('users:api:list-captures')
        self.users_data = baker.make(UserProfile,  _quantity=10)

    def mock_get_response_data(self):
        mocked_response = Mock()

        results = []

        for profile in self.users_data:
            image_key = str(uuid4())
            image_path = f"{image_key}.jpg"

            results.append(
                OrderedDict({
                    "name": profile.user.first_name,
                    "matrice": profile.matrice,
                    "image_path": image_path
                })
            )

        mocked_response.data = OrderedDict({
            "next": None,
            "prev": None,
            "results": results
        })

        return mocked_response

    def test_get_response_status_code(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_get_response_object_bundle(self):
        self.client.get = Mock()
        self.client.get.return_value = self.mock_get_response_data()

        response = self.client.get(self.url)

        data = response.data['results']

        self.assertEquals(
            set(data[0].keys()),
            set(['name', 'matrice', 'image_path'])
        )
