from django.urls import path
from users.api.views import UsersListAPIView

app_name = "users-api"

urlpatterns = [
    path(
        '', UsersListAPIView.as_view(),
        name='users'
    )
]
