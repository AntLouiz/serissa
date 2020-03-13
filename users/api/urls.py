from django.urls import path
from users.api.views import (
    UsersListAPIView,
    UsersCaptureAPIView,
    UsersCaptureDeleteAPIView
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
        'capture/<str:matrice>/<str:image_key>/delete',
        UsersCaptureDeleteAPIView.as_view(),
        name='delete-capture'
    )
]
