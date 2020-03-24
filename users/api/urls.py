from django.urls import path
from users.api.views import (
    UsersProfileListAPIView,
    UsersCaptureAPIView,
    UsersCaptureDeleteAPIView,
    UserCapturesRetrieveAPIView,
    CapturesListAPIView,
)

app_name = "api"

urlpatterns = [
    path(
        '', UsersProfileListAPIView.as_view(),
        name='list'
    ),
    path(
        'capture', UsersCaptureAPIView.as_view(),
        name='capture'
    ),
    path(
        'captures', CapturesListAPIView.as_view(),
        name='captures'
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
