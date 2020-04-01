from django.db import models
from users.models import UserProfile


class CapturePack(models.Model):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(
            self.id,
            self.profile.matrice
        )


class BaseFaceImage(models.Model):
    path = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class FaceImageCapture(BaseFaceImage):
    pack = models.ForeignKey(
        CapturePack,
        on_delete=models.CASCADE,
        related_name='captures'
    )

    def __str__(self):
        return f"{self.pack.profile.user.first_name} {self.created_at}"


class FaceImageAttempt(BaseFaceImage):
    algorithm = models.CharField(max_length=30)
    confidence = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    recognized = models.BooleanField()
    origin = models.CharField(max_length=20)

    def __str__(self):
        return "{} {} {}".format(
            self.algorithm,
            self.confidence,
            self.recognized
        )
