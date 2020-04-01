from rest_framework.generics import ListAPIView
from recognitor.api.serializers import AttemptsModelSerializer
from recognitor.api.paginations import AttemptsPagination
from captures.models import FaceImageAttempt


class AttemptsListAPIView(ListAPIView):

    model = FaceImageAttempt
    serializer_class = AttemptsModelSerializer
    pagination_class = AttemptsPagination

    def get_queryset(self, *args, **kwargs):
        return FaceImageAttempt.objects.all()
