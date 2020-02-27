from rest_framework.generics import ListAPIView
from users.models import Sra010
from users.api.serializers import UserModelSerializer


class UsersListAPIView(ListAPIView):

    model = Sra010
    serializer_class = UserModelSerializer

    def get_queryset(self, *args, **kwargs):
        return Sra010.objects.exclude(d_e_l_e_t_field='*')
