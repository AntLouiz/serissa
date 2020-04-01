from django.urls import reverse
from rest_framework.test import APITestCase
from model_bakery import baker
from captures.models import CapturePack
from captures.api.serializers import CapturePackSerializer
from users.models import UserProfile


class TestCapturesPackListCreateAPIView(APITestCase):

    def setUp(self):
        self.reversed_url = reverse(
            'captures:api:list-create-captures-pack'
        )

        self.capture = baker.make(
            CapturePack,
            is_active=True
        )

        baker.make(
            CapturePack,
            is_active=False,
            _quantity=5
        )

        self.serialized_data = CapturePackSerializer(
            self.capture
        ).data

    def test_get_response_actives_object_bundle(self):
        response = self.client.get(self.reversed_url)

        self.assertEqual(response.status_code, 200)
        data = response.data['results']

        self.assertEqual(
            len(data),
            1
        )

        self.assertEquals(
            data[0],
            self.serialized_data
        )

    def test_sucessfull_post(self):
        matrice = '11111'
        user = baker.make(
            UserProfile,
            matrice=matrice
        )

        data = {
            'user_matrice': user.matrice
        }

        response = self.client.post(
            self.reversed_url,
            data
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            set(response.data.keys()),
            set(self.serialized_data)
        )

    def test_user_not_exists_response_on_post_request(self):
        data = {
            'user_matrice': '545588'
        }

        response = self.client.post(
            self.reversed_url,
            data
        )

        self.assertEqual(
            response.status_code,
            404
        )

    def test_confict_already_exists_active_pack_response_on_post_request(self):
        matrice = '11111'
        profile = baker.make(
            UserProfile,
            matrice=matrice
        )

        data = {
            'user_matrice': profile.matrice
        }

        self.client.post(
            self.reversed_url,
            data
        )

        response = self.client.post(
            self.reversed_url,
            data
        )

        self.assertEqual(response.status_code, 409)

    def test_confict_already_exists_not_active_pack_response_on_post_request(self):
        matrice = '11111'
        profile = baker.make(
            UserProfile,
            matrice=matrice
        )

        data = {
            'user_matrice': profile.matrice
        }

        self.client.post(
            self.reversed_url,
            data
        )

        pack = CapturePack.objects.get(profile=profile)
        pack.is_active = False
        pack.save()

        response = self.client.post(
            self.reversed_url,
            data
        )

        self.assertEqual(response.status_code, 201)
