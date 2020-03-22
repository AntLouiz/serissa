import os
from django.db import models
from users.models import UserProfile


class FaceImage(models.Model):
    path = models.CharField(max_length=200)
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def delete(self, *args, **kwargs):
        os.remove(self.path)
        super(FaceImage, self).delete(*args, **kwargs)


class RecognitionAttempt(models.Model):
    algorithm = models.CharField(max_length=30)
    confidence = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    recognized = models.BooleanField()
    face_image = models.ForeignKey(FaceImage, on_delete=models.CASCADE)
    origin = models.CharField(max_length=20)

    def delete(self, *args, **kwargs):
        face_image = self.face_image
        image_path = face_image.path.rstrip()
        os.remove(image_path)
        super(RecognitionAttempt, self).delete(*args, **kwargs)

    def __str__(self):
        return "{} {} {}".format(
            self.algorithm,
            self.confidence,
            self.recognized
        )
