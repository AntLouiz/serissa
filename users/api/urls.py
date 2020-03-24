from django.urls import path
from users.api.views import (
    ProfilesListAPIView,
    CapturesListAPIView,
    CaptureCreateAPIView,
    CaptureDeleteAPIView,
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
        name='retrieve-captures'
    ),
    path(
        '<str:matrice>/capture/<str:capture_key>/delete',
        CaptureDeleteAPIView.as_view(),
        name='delete-capture'
    ),
]
