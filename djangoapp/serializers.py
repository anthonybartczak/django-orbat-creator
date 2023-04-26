from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Platoon

class PlatoonSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializing all the Platoons
    """
    class Meta:
        model = Platoon
        fields = ('id', 'name', 'country', 'branch', 'platoon_size', 'author_id',)

class PlatoonDetailsSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializing all the Platoons
    """
    class Meta:
        model = Platoon
        fields = ('id', 'name', 'structure')

class PlatoonIdentifiersSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializing all the Platoons
    """
    class Meta:
        model = Platoon
        fields = ('id',)