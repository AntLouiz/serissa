from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    matrice = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.matrice)
