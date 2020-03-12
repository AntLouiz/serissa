from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_202_ACCEPTED,
    HTTP_503_SERVICE_UNAVAILABLE,
)
from serissa.celery import app
from trainings.ws.tasks import process_training
from trainings.api.serializers import (
    TrainingsSerializer,
    TrainingStatusSerializer
)
from serissa.cache import redis_instance


class TrainingAPIView(APIView):

    def post(self, *args, **kwargs):
        celery_inspect = app.control.inspect()
        stats = celery_inspect.stats()

        if stats is None:
            return Response(status=HTTP_503_SERVICE_UNAVAILABLE)

        data = redis_instance.get('training')

        if not data:
            data = redis_instance.set('training', 'pending')

        process_training.delay()

        return Response(status=HTTP_202_ACCEPTED)


class TrainingStatusAPIView(APIView):

    def get(self, request, *args, **kwargs):
        celery_inspect = app.control.inspect()
        stats = celery_inspect.stats()

        data = redis_instance.get('training')

        if not data:
            data = redis_instance.set('training', 'stopped')

        data = data.decode('utf-8')

        if not stats:
            status = 'unavaliable'
            redis_instance.set('training', status)
            data = status

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
