from rest_framework.views import APIView,Response
from src.commons.authentication import IsTest
from rest_framework_jwt.settings import api_settings
from  django.contrib.auth import hashers

from src.serializers.user import UserSerializer
from src.models.user import User
class UserAuthentication(APIView):
    # create token
    def post(self,request):
        username = request.data['username']
        password = request.data['password']

        if username is None or password is None:
            return Response({"success": False, "message": "Tài khoản hoặc mật khẩu không đúng"})
        try:
           user = User.objects.get(username=username)
        except User.DoesNotExist:
           return Response({"success": False, "message": "Tài khoản hoặc mật khẩu không đúng"})

        if hashers.SHA1PasswordHasher().verify(password,user.password):
            user_serializer = UserSerializer(user)
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER(user_serializer.data)
            return Response({"success": True,"token": jwt_encode_handler,"role":user.role,"username":user.username} )
        else:
            return Response({"success": False,"message": "Tài khoản hoặc mật khẩu không đúng"})




    # fresh token

    def get(self, request):
        return Response({'user':'phong'})


