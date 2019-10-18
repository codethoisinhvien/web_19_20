# -*- coding: utf-8 -*-
from rest_framework.views import APIView, Response
from rest_framework import status
from src.commons.authentication import IsTest
from rest_framework_jwt.settings import api_settings
from src.serializers.user import UserSerializer
from src.commons.authentication import JsonWebTokenAuthentication


class ExamRegistrantion(APIView):

    def post(self, request):

        username = request.data['username']
        password = request.data['password']

        user_serializer = UserSerializer(data={"username": username, "password": password})
        try:
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({"success": True, "message": "Đăng kí thành công "}, status.HTTP_200_OK)
            else:
                return Response({"success": False, "message": user_serializer.errors['username']})
        except:
            return Response({"success": False, "message": "Lỗi hệ thống"}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        return Response({'user': 'phong'})

    def delete(self,request):
        pass


