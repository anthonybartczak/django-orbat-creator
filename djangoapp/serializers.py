from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Platoon
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PlatoonSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializing all the Platoons
    """
    class Meta:
        model = Platoon
        fields = ('id', 'name', 'era', 'country', 'branch', 'platoon_size', 'author_id',)

class PlatoonDetailsSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializing all the Platoons
    """
    class Meta:
        model = Platoon
        fields = ('id', 'name', 'era', 'structure', 'notes', 'sources')

class PlatoonCreateSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializing all the Platoons
    """

    class Meta:
        model = Platoon
        fields = ('id', 'name', 'structure', 'author_id', 'branch', 'country', 'description', 'notes', 'sources', 'era')

class PlatoonIdentifiersSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializing all the Platoons
    """
    class Meta:
        model = Platoon
        fields = ('id',)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['id'] = user.id
        token['user'] = user.username
        token['email'] = user.email

        return token