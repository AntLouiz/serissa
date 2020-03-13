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
        matrices = []

        if len(captures_paths):
            users_matrices = [path.split('/')[-1] for path in captures_paths]
            for matrice in users_matrices:
                user_capture_path = BASE_DIR.child('media')\
                    .child('captures').child(matrice.rstrip())

                images = user_capture_path.listdir()

                if len(images):
                    matrices.append(matrice)

        users = Sra010.objects.filter(
            ra_mat__in=matrices
        )

        return users


class UserCapturesRetrieveAPIView(RetrieveAPIView):

    model = Sra010
    serializer_class = UsersCapturesSerializer
    lookup_field = 'ra_mat'

    def get_queryset(self, *args, **kwargs):
        matrice = self.kwargs.get('ra_mat')

        users = Sra010.objects.filter(
            ra_mat=matrice
        )

        return users
