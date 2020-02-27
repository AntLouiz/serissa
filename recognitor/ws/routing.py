from django.urls import path
from .consumers import RecognitorConsumer

websocket_urlpatterns = [
    path('', RecognitorConsumer)
]
