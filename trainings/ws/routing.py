from django.urls import path
from .consumers import TrainingConsumer


websocket_urlpatterns = [
  path('training/<str:channel_key>/', TrainingConsumer)
]
