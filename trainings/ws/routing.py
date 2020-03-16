from django.urls import path
from .consumers import TrainingProgressConsumer


websocket_urlpatterns = [
  path('training/progress', TrainingProgressConsumer)
]
