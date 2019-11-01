from  rest_framework import  serializers
from  src.models.user import Room
from  django.contrib.auth import hashers

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
