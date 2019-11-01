from  rest_framework import  serializers
from  src.models.user import Subject
from  django.contrib.auth import hashers

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
