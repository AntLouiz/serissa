from django.urls import path
from recognitor.api.views import AttemptsListAPIView

app_name = "recognitor-api"

urlpatterns = [
    path(
        'attempts', AttemptsListAPIView.as_view(),
        name='attempts'
    )
]
