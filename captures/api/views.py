from django.shortcuts import get_object_or_404
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_409_CONFLICT,
)
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from captures.models import CapturePack
from users.models import UserProfile
from captures.api.serializers import CapturePackSerializer


class CapturesPackListCreateAPIView(ListCreateAPIView):
    serializer_class = CapturePackSerializer
    queryset = CapturePack.objects.filter(is_active=True)

    def create(self, request, *args, **kwargs):
        matrice = request.data.get('user_matrice')

        profile = get_object_or_404(UserProfile, matrice=matrice)

        exists_pack = CapturePack.objects.filter(
            profile=profile,
            is_active=True
        ).exists()

        if exists_pack:
            return Response(status=HTTP_409_CONFLICT)

        pack = CapturePack(
            profile=profile
        )

        pack.save()

        serializer = self.serializer_class(pack)

        return Response(
            serializer.data,
            status=HTTP_201_CREATED
        )


class CapturesPackRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CapturePack.objects.all()
    serializer_class = CapturePackSerializer
