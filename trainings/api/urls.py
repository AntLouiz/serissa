
from django.urls import path
from .views import TrainingAPIView, TrainingChannelsListAPIView

app_name = "trainings-api"

urlpatterns = [
    path(
        '', TrainingAPIView.as_view(),
        name='trainings'
    ),
    path(
        'channels', TrainingChannelsListAPIView.as_view(),
        name='trainings-channels'
    )
]
