from rest_framework.generics import ListAPIView, RetrieveAPIView
from users.models import Zq1010, Sra010
from recognitor.api.serializers import (
    AttemptsModelSerializer,
    CapturesSerializer,
    UsersCapturesSerializer
)
from serissa.settings import BASE_DIR


class AttemptsListAPIView(ListAPIView):

    model = Zq1010
    serializer_class = AttemptsModelSerializer

    def get_queryset(self, *args, **kwargs):
        return Zq1010.objects.exclude(d_e_l_e_t_field='*')


class CapturesListAPIView(ListAPIView):

    model = Sra010
    serializer_class = CapturesSerializer

    def get_queryset(self, *args, **kwargs):
        captures_folder = BASE_DIR.child("media").child("captures")
        captures_paths = captures_folder.listdir()
        users_matrices = []

        if len(captures_paths):
            users_matrices = [path.split('/')[-1] for path in captures_paths]

        users = Sra010.objects.filter(
            ra_mat__in=users_matrices
        )

        return users


class UserCapturesRetrieveAPIView(RetrieveAPIView):

    model = Sra010
    serializer_class = UsersCapturesSerializer
    lookup_field = 'ra_mat'

    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        matrice = self.kwargs.get('ra_mat')

        users = Sra010.objects.filter(
            ra_mat=matrice
        )

        return users
