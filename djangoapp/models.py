from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres import fields
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
    era = fields.IntegerRangeField(null=True)
    country = models.CharField(max_length=255, null=True)
    branch = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=255, null=True)
    notes = models.JSONField(null=True)
    sources = models.JSONField(null=True)
    structure = models.JSONField(null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def platoon_size(self):
        if self.structure:
            return self.structure["size"];