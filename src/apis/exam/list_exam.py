# -*- coding: utf-8 -*-
from rest_framework.views import APIView, Response
from rest_framework import status

from rest_framework_jwt.settings import api_settings
from src.serializers.exam import ExamSerializer
from src.serializers.seat_room import RoomSeatSerializer
from src.models import Exam,RoomSeat
from src.commons.authentication import JsonWebTokenAuthentication
from src.commons.permission import IsAdmin

from rest_framework.decorators import permission_classes
class ListExamAPI(APIView):
     # lấy  danh sách  kì thi
     authentication_classes = [JsonWebTokenAuthentication]
     def get(self, request):
        exam_name= request.GET.get('exam')
        if(exam_name is None):
            exam_name=''
        try:
         exam = Exam.objects.filter(name__contains=exam_name)
         examSerializer = ExamSerializer(exam,many=True)
         return  Response({"success":True,"exams":examSerializer.data})
        except Exception as e :
          return Response({"success": False, "message": "Có lỗi xảy ra"})

     # tao kì thi
     @permission_classes([IsAdmin])
     def post(self, request):

         exam_serializer=ExamSerializer(data=request.data);
         if exam_serializer.is_valid():
             exam_serializer.save()
             return Response({'success': True,"message":"Tạo kì thi thành công ","exam_id":exam_serializer.data['id']})
         else:
             return Response({'success': False,"message":"Tạo kì thi thất bại","error":exam_serializer.errors})




