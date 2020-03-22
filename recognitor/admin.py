from django.contrib import admin
from .models import FaceImage, RecognitionAttempt

admin.site.register(FaceImage)
admin.site.register(RecognitionAttempt)
