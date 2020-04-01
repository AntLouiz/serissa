from django.urls import path, include

app_name = 'captures'

urlpatterns = [
    path(
        '',
        include(('captures.api.urls'), namespace='api')
    )
]
