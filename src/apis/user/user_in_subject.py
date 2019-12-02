from rest_framework.views import APIView, Response
from rest_framework import status
from src.commons.authentication import IsTest
from rest_framework_jwt.settings import api_settings
from src.serializers.user_subject import ExamUserSubject
from src.commons.authentication import JsonWebTokenAuthentication



class UserInSubjectApi(APIView):
    # tạo thí sinh đăng kí
    def put(self, request,id):
      data = {"be_register":"True"}
      user_subject = ExamUserSubject();
      user_subject.update(1,True)
      return Response({'user': 'giang'})
    # lấy ra danh sách
    def get(self, request,id):
        user_subject = ExamUserSubject.objects.get(pk=id);
        user_subject.delete()
        return Response({ 'success':True,"message":"Thành công"})

    def delete(self,request,id):
        user_subject =ExamUserSubject.objects.get(pk=id)
        user_subject.delete()
        return Response({'user': 'giang'})