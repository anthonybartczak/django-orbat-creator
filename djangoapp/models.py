from django.db import models
from django.contrib.auth.models import User
import uuid
import json

# Create your models here.

class Platoon(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
    )
    objects = models.Manager
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, null=True)
    branch = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=255, null=True)
    structure = models.JSONField(null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    @property
    def platoon_size(self):
        return self.structure["size"];