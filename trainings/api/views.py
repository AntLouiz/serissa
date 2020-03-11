import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_202_ACCEPTED,
    HTTP_404_NOT_FOUND
)
from trainings.ws.tasks import process_training
from trainings.api.serializers import (
    TrainingsSerializer,
    TrainingStatusSerializer
)
from serissa.cache import redis_instance


class TrainingAPIView(APIView):

    def post(self, *args, **kwargs):
        data = redis_instance.get('training')
        if not data:
            data = redis_instance.set('training', 'stopped')

        process_training.delay()

        return Response(status=HTTP_202_ACCEPTED)


class TrainingStatusAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = redis_instance.get('training')
        if not data:
            data = redis_instance.set('training', 'stopped')

        data = data.decode('utf-8')
        serializer = TrainingStatusSerializer({'status': data})

        return Response(status=HTTP_200_OK, data=serializer.data)


class TrainingChannelsListAPIView(APIView):

    def get(self, *args, **kwargs):
        data = [{
            'name': 'Face Recognition',
            'channel_key': 'face_recognition'
        }]

        serializer = TrainingsSerializer(data, many=True)

        return Response(status=HTTP_200_OK, data=serializer.data)
