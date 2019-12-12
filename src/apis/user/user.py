from django.contrib.auth import hashers
from rest_framework.views import APIView, Response

from src.models.user import User


class UserApi(APIView):
    # sưa thong tin tai khoan
    def put(self, request, id=None):
        print(request.data)

        try:
            user = User.objects.get(pk=id);
            print(user)
            user.full_name = request.data['full_name']
            user.code = request.data['code']
            user.username = request.data['username']
            user.role = request.data['role']
            user.save()
            return Response({"success": True, "message": "Thay đổi thành cônng"}, )

        except Exception as e:
            print(e)
            return Response({"success": True, "message": "Thay đổi thất bại"}, )

    #  sưa password

    def patch(self, request, id=None):
        print(request.data)
        try:
            user = User.objects.get(pk=id);
            user.password = hashers.SHA1PasswordHasher().encode(request.data['password'], salt='1123')
            user.save()
            return Response({"success": True, "message": "Thay đổi thành cônng"}, )

        except Exception as e:
            print(e)
            return Response({"success": True, "message": "Thay đổi thất bại"}, )

    #  xóa tài khoản

    def delete(self, request, id=None):
        try:
            user = User.objects.get(pk=id)
            print(user)
            user.delete()
            return Response({"success": True, "message": "Xóa thành công"}, )

        except Exception as e:
            print(e)
            return Response({"success": False, "message": "Xóa thất bại"}, )
