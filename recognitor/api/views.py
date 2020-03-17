from rest_framework.generics import ListAPIView
from recognitor.models import Zq1010
from recognitor.api.serializers import AttemptsModelSerializer
from recognitor.api.paginations import AttemptsPagination


class AttemptsListAPIView(ListAPIView):

    model = Zq1010
    serializer_class = AttemptsModelSerializer
    pagination_class = AttemptsPagination

    def get_queryset(self, *args, **kwargs):
        return Zq1010.objects.exclude(d_e_l_e_t_field='*')
