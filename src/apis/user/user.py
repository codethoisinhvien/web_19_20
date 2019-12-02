from rest_framework.views import APIView, Response
from rest_framework import status
from src.commons.authentication import IsTest
from rest_framework_jwt.settings import api_settings
from src.serializers.user import UserSerializer
from src.commons.authentication import JsonWebTokenAuthentication



class UserApi(APIView):
    # đăng kí tài khoản
    def post(self, request):

        username = request.data['username']
        password = request.data['password']
        print(password)
        code = request.data['code']
        full_name = request.data['full_name']
        role = 1

        user_serializer = UserSerializer(
            data={"username": username, "password": password, "code": code, "full_name": full_name, "role": 1})
        try:
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({"success": True, "message": "Đăng kí thành công "}, status.HTTP_200_OK)
            else:
                print(user_serializer.errors)
                return Response({"success": False, "message": user_serializer.errors})
        except Exception as e:
            print(e)
            return Response({"success": False, "message": "Lỗi hệ thống"})

    # lấy thông tin tài khoản
    def get(self, request):
        return Response({'user': 'giang'})

    # sửa thông tin tài khoản
    def put(self, request):
        user_serializer = UserSerializer()

        user_serializer.updatePassword(1,{"old_password":"123456787","new_passord":"17200705"})
        return Response({"success": True, "message": "Thay đổi thành cônng"},)

    #  xóa tài khoản
    def delete(self, request):
        pass
