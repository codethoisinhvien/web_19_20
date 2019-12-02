from  rest_framework import  serializers
from  src.models.user import ExamUserSubject
from  django.contrib.auth import hashers

class BandUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamUserSubject
        fields = ('id','username','password','role','code','full_name')
    def save(self, **kwargs):
       pass