from django.contrib import admin
from captures.models import FaceImageAttempt, FaceImageCapture


admin.site.register(FaceImageCapture)
admin.site.register(FaceImageAttempt)
