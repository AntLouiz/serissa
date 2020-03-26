from unittest.mock import Mock
from uuid import uuid4
from django.urls import reverse
from rest_framework.test import APITestCase


class TestCaptureCreateAPIView(APITestCase):

    def setUp(self):
        self.url = reverse('users:api:create-capture')
        # self.client.post = Mock()

    def mock_limit_exceeded_response(self):
        mocked_response = Mock()
        msg = 'Accepted only 15 photos peer users'

        mocked_response.status_code = 403

        mocked_response.data = {
            'message': msg
        }

        return mocked_response

    def test_post_without_correct_data(self):
        response = self.client.post(self.url)
        expected_message = 'Must contain the matrice and images.'

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['message'], expected_message)

    def test_post_captures_limit_exceeded(self):
        mocked_client = Mock()
        mocked_client.post.return_value = self.mock_limit_exceeded_response()

        images_files = []

        for file in range(16):
            file = Mock()
            file.name = uuid4()
            images_files.append(file)

        data = {
            'matrice': '11111',
            'images': images_files
        }

        response = mocked_client.post(
            self.url,
            data=data,
            content_type='multipart/form-data'
        )
        expected_message = 'Accepted only 15 photos peer users'

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['message'], expected_message)
