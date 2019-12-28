from rest_framework import serializers

from src.models import ExamUserSubject


class BandUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamUserSubject
        fields = ('id', 'username', 'password', 'role', 'code', 'full_name')

    def save(self, **kwargs):
        pass
