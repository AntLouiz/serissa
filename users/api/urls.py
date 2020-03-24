from django.urls import path
from users.api.views import (
    ProfilesListAPIView,
    CapturesListAPIView,
    CaptureCreateAPIView,
    UsersCaptureDeleteAPIView,
    CapturesRetrieveAPIView
)

app_name = "api"

urlpatterns = [
    path(
        '', ProfilesListAPIView.as_view(),
        name='list-profiles'
    ),
    path(
        'capture', CaptureCreateAPIView.as_view(),
        name='create-capture'
    ),
    path(
        'captures', CapturesListAPIView.as_view(),
        name='list-captures'
    ),
    path(
        '<str:matrice>/captures', CapturesRetrieveAPIView.as_view(),
        name='captures-retrieve'
    ),
    path(
        'capture/<str:matrice>/<str:image_key>/delete',
        UsersCaptureDeleteAPIView.as_view(),
        name='delete-capture'
    ),
]
