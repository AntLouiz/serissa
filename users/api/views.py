from rest_framework.generics import ListAPIView
from users.models import UserProfile
from users.api.serializers import UserProfileSerializer


class ProfilesListAPIView(ListAPIView):

    model = UserProfile
    serializer_class = UserProfileSerializer

    def get_queryset(self, *args, **kwargs):
        return UserProfile.objects.all()
