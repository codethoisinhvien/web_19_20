# -*- coding: utf-8 -*-

from django.db.models import Q
from django.db.utils import IntegrityError
from rest_framework.views import APIView, Response

from src.commons.utils import check_schedule_in_room
from src.models import ExamRoomSubject
from src.serializers.schedule import ScheduleSerializer, ScheduleCreateSerializer
from src.commons.authentication import JsonWebTokenAuthentication
from src.commons.permission import IsAdmin
class ScheduleAPI(APIView):
    authentication_classes = [JsonWebTokenAuthentication]
    permission_classes = [IsAdmin]
    def get(self, request, id=None):
        try:
            condition = Q()
            exam_name = request.GET.get('exam')
            room_id = request.GET.get('room')
            subject_id = request.GET.get('subject')
            day = request.GET.get('day')
            if (room_id is not None and room_id != ''):
                condition = condition & Q(room_id=room_id)
            if (exam_name is not None):
                condition = condition & Q(exam_id__name__contains=exam_name)
            if (subject_id is not None and (subject_id != '')):
                condition = condition & Q(subject_id=subject_id)
            if (day is not None and (day != '')):
                condition = condition & Q(day=day)

            schedule = ExamRoomSubject.objects.all().select_related('room_id').select_related('exam_id').select_related(
                'subject_id').order_by('time_start').filter(condition)
            scheduleSerializer = ScheduleSerializer(schedule, many=True)
            return Response({"success": True, "schedules": scheduleSerializer.data})
        except Exception as e:
            return Response({"success": False, "message": "Có lỗi xảy ra"})

    def put(self, request, id):
        print(request.data)
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

    def post(self, request, id=None):
        scheduleSerializer = ScheduleCreateSerializer(data=request.data)
        check_schedule_in_room(request.data['room_id'], request.data['day'], request.data['start_time'],
                               request.data['end_time'])
        print(request.data)

        if scheduleSerializer.is_valid():

            try:
                data = scheduleSerializer.save()
                return Response({"success": True, 'message': "Tạo ca thi thành công", 'schedule_id': data.id})
            except IntegrityError as e:
                print(e)
                return Response({"success": False, 'message': "Bản ghi đã tồn tại"})
        else:
            return Response({"success": False, "message": scheduleSerializer.errors})

    def delete(self, request, id):
        try:

            schedule = ExamRoomSubject.objects.get(pk=id)
            schedule.delete()
            return Response({"success": True, 'message': "Xóa bản ghi thành công"})
        except ExamRoomSubject.DoesNotExist:
            return Response({"success": False, 'message': "Ca thi  không tồn tại"})
        except Exception as e:
            print(e)
            return Response({"success": False, 'message': "Hệ  thông có lỗi"})
