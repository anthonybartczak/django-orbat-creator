from rest_framework import serializers
from .models import Platoon

class PlatoonSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializing all the Platoons
    """
    class Meta:
        model = Platoon
        fields = ('id', 'name', 'author_id', 'platoon_size')