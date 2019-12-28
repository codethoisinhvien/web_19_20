from rest_framework.views import APIView, Response

from src.commons.authentication import JsonWebTokenAuthentication
from src.commons.permission import IsAdmin
from src.models.user import User
from src.serializers.user import ListUserSerializer
from src.serializers.user import UserSerializer


class ListUser(APIView):
    authentication_classes = [JsonWebTokenAuthentication]
    permission_classes = [IsAdmin]

    def post(self, request):
        user_serializer = UserSerializer(
            data=request.data)
        try:
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({"success": True, "message": "Đăng kí thành công "})
            else:
                print(user_serializer.errors)
                return Response({"success": False, "message": user_serializer.errors})
        except Exception as e:
            print(e)
            return Response({"success": False, "message": "Lỗi hệ thống"})

    def get(self, request):
        code = request.GET.get('code')
        page = request.GET.get('page')
        print(page)
        if page is None:
            page = 0
        if (code is None):
            code = ''
        user = User.objects.filter(code__contains=code).order_by('-id')[int(page) * 10:(int(page) + 1) * 10];
        userSerializer = ListUserSerializer(user, many=True)
        return Response({"success": True, 'users': userSerializer.data})
