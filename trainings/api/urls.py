
from django.urls import path
from .views import (
    TrainingAPIView,
    TrainingChannelsListAPIView,
    TrainingStatusAPIView,
)

app_name = "trainings-api"

urlpatterns = [
    path(
        '', TrainingAPIView.as_view(),
        name='trainings'
    ),
    path(
        'channels', TrainingChannelsListAPIView.as_view(),
        name='trainings-channels'
    ),
    path(
        'status', TrainingStatusAPIView.as_view(),
        name='trainings-status'
    )
]
