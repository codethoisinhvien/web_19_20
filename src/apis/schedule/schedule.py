# -*- coding: utf-8 -*-
from rest_framework.views import APIView, Response
from rest_framework import status
from src.serializers.schedule import ScheduleSerializer, ScheduleCreateSerializer
from src.models.user import ExamRoomSubject, Exam, Subject, Room
from django.db.utils import IntegrityError



class ScheduleAPI(APIView):
    #
    def get(self, request, id=None ):
        schedule = ExamRoomSubject.objects.all().select_related('room_id').select_related('exam_id').select_related(
            'subject_id').order_by("id")
        scheduleSerializer = ScheduleSerializer(schedule, many=True)
        return Response({"success": True, "schedules": scheduleSerializer.data})

    def put(self, request,id):
        scheduleSerializer = ScheduleCreateSerializer(data=request.data)
        if scheduleSerializer.is_valid():

            try:
                scheduleSerializer.update(ExamRoomSubject.objects.get(pk=id))
                return Response({"success": True, 'message': "Thay đổi thành công "})
            except IntegrityError as e:
                print(e)
                return Response({"success": False, 'message': "Bản ghi đã tồn tại"})
            except Exception as e:
                print(e)
                return Response({"success": False, 'message': str(e)})
        else:
            return Response({"success": False, "message": scheduleSerializer.errors})

    def post(self, request,id=None):
        print(request.data)
        scheduleSerializer = ScheduleCreateSerializer(data=request.data)
        if scheduleSerializer.is_valid():

             try:
                scheduleSerializer.save()
                return Response({"success": True, 'message': "Tạo ca thi thành công"})
             except IntegrityError as e:
                print(e)
                return Response({"success": False, 'message':"Bản ghi đã tồn tại"})
        else:
            return Response({"success": False, "message": scheduleSerializer.errors})

    def delete(self, request,id):
        try:

           schedule =  ExamRoomSubject.objects.get(pk=id)
           schedule.delete()
           return Response({"success": True, 'message': "Xóa bản ghi thành công"})
        except ExamRoomSubject.DoesNotExist:
         return Response({"success": False, 'message': "Ca thi  không tồn tại"})
        except Exception as e :
            print(e)
            return Response({"success": False, 'message': "Hệ  thông có lỗi"})
