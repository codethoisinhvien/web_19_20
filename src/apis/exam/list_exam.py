# -*- coding: utf-8 -*-
from rest_framework.views import APIView, Response
from rest_framework import status
from src.commons.authentication import IsTest
from rest_framework_jwt.settings import api_settings
from src.serializers.exam import ExamSerializer
from src.serializers.seat_room import RoomSeatSerializer
from src.models.user import Exam,RoomSeat
from src.commons.authentication import JsonWebTokenAuthentication


class ListExamAPI(APIView):
     #
     def get(self, request):
        exam = Exam.objects.all()
        examSerializer = ExamSerializer(exam,many=True)
        return  Response({"success":True,"exams":examSerializer.data})

     def put(self, request):
         a = RoomSeat.objects.filter(room_id=1).select_related('room_id').select_related('seat_id')
         c = RoomSeatSerializer(a);
         print(c.data)
         b = [{"room":item.room_id.name,"seat":item.seat_id.name} for item in a]
         return Response({'user': b})

     def post(self, request):
         print(request.data)
         exam_serializer=ExamSerializer(data=request.data);
         if exam_serializer.is_valid():
             exam_serializer.save()
             return Response({'success': True,"message":"Tạo kì thi thành công ","exam_id":exam_serializer.data['id']})
         else:
             return Response({'success': False,"message":"Tạo kì thi thất bại","error":exam_serializer.errors})




