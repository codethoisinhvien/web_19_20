from rest_framework.views import APIView, Response
from rest_framework import status
from src.commons.authentication import IsTest
from rest_framework_jwt.settings import api_settings
from src.serializers.user import UserSerializer
from src.commons.authentication import JsonWebTokenAuthentication



class ListAllowedStudentApi(APIView):
    # tạo thí sinh đăng kí
    def post(self, request):
      pass
    # lấy ra danh sách
    def get(self, request):
        return Response({'user': 'giang'})

