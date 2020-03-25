from django.urls import reverse
from rest_framework.test import APITestCase
from model_bakery import baker
from users.models import UserProfile
from users.api.serializers import UserProfileSerializer


class TestProfilesListAPIView(APITestCase):

    def setUp(self):
        self.url = reverse('users:api:list-profiles')
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
