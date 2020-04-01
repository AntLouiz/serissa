from django.urls import path
from captures.api.views import (
    CapturesPackListCreateAPIView,
    CapturesPackRetrieveUpdateDestroyAPIView
)

app_name = "api"

urlpatterns = [
    path(
        '', CapturesPackListCreateAPIView.as_view(),
        name='list-create-captures-pack'
    ),
    path(
        '<int:pk>', CapturesPackRetrieveUpdateDestroyAPIView.as_view(),
        name='retrieve-update-destroy-captures-pack'
    )
]
