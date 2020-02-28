from django.urls import path
from users.api.views import UsersListAPIView, UsersCaptureAPIView

app_name = "users-api"

urlpatterns = [
    path(
        '', UsersListAPIView.as_view(),
        name='users'
    ),
    path(
        'capture', UsersCaptureAPIView.as_view(),
        name='capture'
    )
]
