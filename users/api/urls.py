from django.urls import path
from users.api.views import ProfilesListAPIView


app_name = "api"

urlpatterns = [
    path(
        '', ProfilesListAPIView.as_view(),
        name='list-profiles'
    )
]
