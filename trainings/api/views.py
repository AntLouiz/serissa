from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_202_ACCEPTED
)
from trainings.ws.tasks import process_training
from trainings.api.serializers import TrainingsSerializer


class TrainingAPIView(APIView):

    def post(self, *args, **kwargs):
        process_training.delay()
        return Response(status=HTTP_202_ACCEPTED)


class TrainingChannelsListAPIView(APIView):

    def get(self, *args, **kwargs):
        data = [{
            'name': 'Face Recognition',
            'channel_key': 'face_recognition'
        }]

        serializer = TrainingsSerializer(data, many=True)

        return Response(status=HTTP_200_OK, data=serializer.data)
