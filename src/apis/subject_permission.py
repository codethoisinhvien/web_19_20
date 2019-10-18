# -*- coding: utf-8 -*-
from rest_framework.views import APIView, Response
from rest_framework import status
from src.commons.authentication import IsTest
from rest_framework_jwt.settings import api_settings
from src.serializers.user import UserSerializer
from src.commons.authentication import JsonWebTokenAuthentication


class SubjectPermission(APIView):
    # tao quyền được thi và cấm thi
    def post(self, request):
        pass

    def get(self, request):
        return Response({'user': 'phong'})
    # sửa quyền

    def put(self,request):
        pass
    # xóa mối quan hệ
    def delete(self,request):
        pass


