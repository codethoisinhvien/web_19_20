from rest_framework import serializers

from src.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    code = serializers.CharField()

    class Meta:
        model = Subject
        fields = '__all__'
