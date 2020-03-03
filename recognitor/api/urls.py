from django.urls import path
from recognitor.api.views import AttemptsListAPIView, CapturesListAPIView

app_name = "recognitor-api"

urlpatterns = [
    path(
        'attempts', AttemptsListAPIView.as_view(),
        name='attempts'
    ),
    path(
        'captures', CapturesListAPIView.as_view(),
        name='captures'
    )
]
