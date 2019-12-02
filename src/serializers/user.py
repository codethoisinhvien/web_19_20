from  rest_framework import  serializers
from  src.models.user import User
from  django.contrib.auth import hashers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','role','code','full_name')
    def save(self, **kwargs):
        print(self.validated_data['username'])
        user = User(
            username=self.validated_data['username'],

            password = hashers.SHA1PasswordHasher().encode(self.validated_data['password'],salt='1123'),
            full_name=self.validated_data['full_name'],
            code = self.validated_data['code'],
            role= self.validated_data['role']
        )
        user.save()
    def updatePassword(self, id, validated_data):
        instance = User.objects.get(pk=id)
        if hashers.SHA1PasswordHasher().verify(validated_data['old_password'],  instance.password):
          instance.password = hashers.SHA1PasswordHasher().encode(validated_data['new_password'],salt='1123')
          instance.save()
        else:
          raise Exception("Mật khẩu cũ không đúng")

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','role','code','full_name')

