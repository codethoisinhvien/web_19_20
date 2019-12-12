from rest_framework.views import APIView, Response

from src.models.user import User
from src.serializers.user import ListUserSerializer
from src.serializers.user import UserSerializer


class ListUser(APIView):

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

    def get(self, request):
        code=request.GET.get('code')
        print(code)
        if(code is None):
            code=''
        role = 1

        user = User.objects.filter(code__contains=code );

        userSerializer = ListUserSerializer(user, many=True)
        return Response({"success": True, 'users': userSerializer.data})

    def put(self, request):
        pass

    # xóa mối quan hệ
    def delete(self, request):
        pass
