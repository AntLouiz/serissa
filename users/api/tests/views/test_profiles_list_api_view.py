import json
from rest_framework.test import APITestCase
from rest_framework.pagination import LimitOffsetPagination
from model_bakery import baker
from users.models import UserProfile
from users.api.serializers import UserProfileSerializer


class TestProfilesListAPIView(APITestCase):

    def setUp(self):
        self.url = '/users/api/'
        self.users_data = baker.make(UserProfile,  _quantity=10)

    def test_get_response_status_code(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_get_response_object_bundle(self):
        response = self.client.get(self.url)

        data = response.data
        data = data['results']

        serializer = UserProfileSerializer(self.users_data, many=True)

        self.assertEqual(
            data,
            serializer.data
        )
