from unittest.mock import Mock
from uuid import uuid4
from collections import OrderedDict
from django.urls import reverse
from rest_framework.test import APITestCase
from model_bakery import baker
from users.models import UserProfile


class TestCapturesRetrieveAPIView(APITestCase):

    def setUp(self):
        self.matrice = '11111'

        self.user_profile = baker.make(
            UserProfile,
            matrice=self.matrice
        )

        self.url = reverse(
            'users:api:retrieve-captures',
            kwargs={
                'matrice': self.matrice
            }
        )

        self.client.get = Mock()
        self.client.get.return_value = self.mock_get_response_data()

    def mock_get_response_data(self):
        mocked_response = Mock()

        profile = UserProfile.objects.filter(
            matrice=self.matrice
        ).first()

        data = {
            'matrice': profile.matrice,
            'name': profile.user.first_name,
            'captures_paths': ['{}.jpg'.format(uuid4()) for i in range(10)]
        }

        mocked_response.data = OrderedDict(data)
        mocked_response.status_code = 200

        return mocked_response

    def test_get_response_status_code(self):
        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            200
        )

    def test_get_response_object_bundle(self):
        response = self.client.get(self.url)

        data = response.data

        self.assertEquals(
            set(data.keys()),
            set(['name', 'matrice', 'captures_paths'])
        )
