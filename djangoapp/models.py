from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Platoon(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255)
    platoon = models.JSONField(null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    @property
    def platoon_size(self):
        return 0;