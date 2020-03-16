from django.urls import path
from users.api.views import (
    UsersListAPIView,
    UsersCaptureAPIView,
    UsersCaptureDeleteAPIView,
    UserCapturesRetrieveAPIView,
    CapturesListAPIView,
)

app_name = "users-api"

urlpatterns = [
    path(
        '', UsersListAPIView.as_view(),
        name='users'
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
        'captures/<str:ra_mat>', UserCapturesRetrieveAPIView.as_view(),
        name='user-captures'
    ),
    path(
        'capture/<str:matrice>/<str:image_key>/delete',
        UsersCaptureDeleteAPIView.as_view(),
        name='delete-capture'
    ),
]
