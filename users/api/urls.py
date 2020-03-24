from django.urls import path
from users.api.views import (
    ProfilesListAPIView,
    CapturesListAPIView,
    CaptureCreateAPIView,
    UsersCaptureDeleteAPIView,
    UserCapturesRetrieveAPIView
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
        'captures/<str:matrice>', UserCapturesRetrieveAPIView.as_view(),
        name='user-captures'
    ),
    path(
        'capture/<str:matrice>/<str:image_key>/delete',
        UsersCaptureDeleteAPIView.as_view(),
        name='delete-capture'
    ),
]
