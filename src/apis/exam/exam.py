# -*- coding: utf-8 -*-
from rest_framework.views import APIView, Response
from rest_framework import status

from rest_framework_jwt.settings import api_settings
from src.serializers.exam import ExamSerializer
from src.models.user import Exam
from src.commons.authentication import JsonWebTokenAuthentication


class ExamAPI(APIView):
     #
     def get(self, request,id=None):
        exam = Exam.objects.get(id=id)
        examSerializer = ExamSerializer(exam,many=True)
        return  Response({"success":True,"exam":examSerializer.data})





     def post(self, request):

        exam = Exam(name="Thi hoc ki 1",status=True)
        exam.save()
        return Response({'success':"true"})



     def put(self, request,id=None):
         print(id)
         exam = Exam.objects.get(id=id)
         exam_serializer = ExamSerializer(data=request.data);
         if exam_serializer.is_valid():
             exam_serializer.update(exam,exam_serializer.validated_data)
             return Response(
                 {'success': True, "message": "Sửa kì thi thành công "})
         else:
             return Response({'success': False, "message": "Sửa kì thi thất bại", "error": exam_serializer.errors})


     def delete(self,request,id=None):
         try:
           exam = Exam.objects.get(id=id)
           exam.delete()
           return Response({'success': True,"message":"Xóa kì thi thành công"})
         except Exception as e:
            print(e)
            return Response({'success': True, "message": "Xóa kì thi thành công","erro":e})




