from  rest_framework import  serializers
from  src.models.user import User
from  django.contrib.auth import hashers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','role')
    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],

            password = hashers.SHA1PasswordHasher().encode(self.validated_data['password'],salt='1123')
        )
        user.save()
