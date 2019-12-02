from  rest_framework import  serializers
from  src.models.user import Exam
from  django.contrib.auth import hashers

class ExamSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = Exam
        fields = ('id','name','status')
