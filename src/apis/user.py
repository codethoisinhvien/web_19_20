from rest_framework.views import APIView, Response
from rest_framework import status
from src.commons.authentication import IsTest
from rest_framework_jwt.settings import api_settings
from src.serializers.user import UserSerializer
from src.commons.authentication import JsonWebTokenAuthentication


class User(APIView):
    #đăng kí tài khoản
    def post(self, request):

        username = request.data['username']
        password = request.data['password']
        print(password)
        code = request.data['code']
        full_name = request.data['full_name']
        role = 1







        user_serializer = UserSerializer(data={"username": username, "password": password,"code":code,"full_name":full_name,"role":1})
        try:
         if user_serializer.is_valid():
                user_serializer.save()
                return Response({"success": True, "message": "Đăng kí thành công "}, status.HTTP_200_OK)
         else:
               print(user_serializer.errors)
               return Response({"success": False, "message": user_serializer.errors})
        except :
               return Response({"success": False, "message": "Lỗi hệ thống"}, status.HTTP_500_INTERNAL_SERVER_ERROR)
    # lấy thông tin tài khoản
    def get(self, request):
        return Response({'user': 'phong'})
    # sửa thông tin tài khoản
    def put(self,request):
        pass

    #  xóa tài khoản
    def put(self, request):
            pass


