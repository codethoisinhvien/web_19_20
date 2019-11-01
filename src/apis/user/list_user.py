from src.serializers.user import ListUserSerializer
from src.models.user import  User
from src.commons.authentication import JsonWebTokenAuthentication
from rest_framework.views import APIView, Response

class ListUser(APIView):

    def post(self, request):
      pass

    # get user
    def get(self, request):
        role =1
        user = User.objects.filter(role =role);

        userSerializer = ListUserSerializer(user,many=True)
        return Response({"success":True,'users': userSerializer.data})


    def put(self,request):
        pass
    # xóa mối quan hệ
    def delete(self,request):
        pass
