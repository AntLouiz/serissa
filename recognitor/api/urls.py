from django.urls import path
from recognitor.api.views import (
    AttemptsListAPIView,
    CapturesListAPIView,
    UserCapturesRetrieveAPIView
)

app_name = "recognitor-api"

urlpatterns = [
    path(
        'attempts', AttemptsListAPIView.as_view(),
        name='attempts'
    ),
    path(
        'captures', CapturesListAPIView.as_view(),
        name='captures'
    ),
    path(
        'captures/<str:ra_mat>', UserCapturesRetrieveAPIView.as_view(),
        name='user-captures'
    )
]
