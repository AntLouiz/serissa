from rest_framework.generics import ListAPIView
from users.models import Zq1010
from recognitor.api.serializers import AttemptsModelSerializer


class AttemptsListAPIView(ListAPIView):

    model = Zq1010
    serializer_class = AttemptsModelSerializer

    def get_queryset(self, *args, **kwargs):
        return Zq1010.objects.exclude(d_e_l_e_t_field='*')
