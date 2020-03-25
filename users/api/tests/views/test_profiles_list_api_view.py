from django.test import TestCase


class TestProfilesListAPIView(TestCase):

    def setUp(self):
        self.url = '/users/api/'

    def test_get_response_status_code(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
