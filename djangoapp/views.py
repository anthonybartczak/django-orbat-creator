from django.shortcuts import render
from django.http import HttpResponse
from djangoapp.serializers import PlatoonSerializer
from .models import Platoon
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
# Create your views here.


class PlatoonsView(viewsets.ModelViewSet):
    queryset = Platoon.objects.all()
    serializer_class = PlatoonSerializer