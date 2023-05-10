from djangoapp.serializers import \
PlatoonSerializer, PlatoonDetailsSerializer, PlatoonIdentifiersSerializer, PlatoonCreateSerializer, UserSerializer, CustomTokenObtainPairSerializer
from .models import Platoon, User
from rest_framework import viewsets, views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers

# Create your views here.

class PlatoonsView(viewsets.ModelViewSet):
    queryset = Platoon.objects.all()
    serializer_class = PlatoonSerializer

    @action(methods=['get'], detail=True)
    def details(self, request, pk=None):
        queryset = Platoon.objects.filter(id=pk)
        serializer = PlatoonDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

class PlatoonsCreateView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Platoon.objects.all()
    serializer_class = PlatoonCreateSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get('user_id')
        try:
            author = User.objects.get(id=user_id)
        except User.DoesNotExist:
            author = self.request.user
        serializer.save(author=author)

class PlatoonsIdentifiersView(viewsets.ModelViewSet):
    queryset = Platoon.objects.all()
    serializer_class = PlatoonIdentifiersSerializer

class LoadUserView(views.APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )

        except:
            return Response(
                {'error': 'Something went wrong with loading the user!'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer