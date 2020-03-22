from rest_framework.generics import ListAPIView
from recognitor.models import RecognitionAttempt
from recognitor.api.serializers import AttemptsModelSerializer
from recognitor.api.paginations import AttemptsPagination


class AttemptsListAPIView(ListAPIView):

    model = RecognitionAttempt
    serializer_class = AttemptsModelSerializer
    pagination_class = AttemptsPagination

    def get_queryset(self, *args, **kwargs):
        return RecognitionAttempt.objects.all()
