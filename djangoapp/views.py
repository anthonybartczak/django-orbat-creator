from djangoapp.serializers import PlatoonSerializer, PlatoonDetailsSerializer, PlatoonIdentifiersSerializer
from .models import Platoon
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class PlatoonsView(viewsets.ModelViewSet):
    queryset = Platoon.objects.all()
    serializer_class = PlatoonSerializer

    @action(methods=['get'], detail=True)
    def details(self, request, pk=None):
        queryset = Platoon.objects.filter(id=pk)
        serializer = PlatoonDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

class PlatoonsIdentifiersView(viewsets.ModelViewSet):
    queryset = Platoon.objects.all()
    serializer_class = PlatoonIdentifiersSerializer