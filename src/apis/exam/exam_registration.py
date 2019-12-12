# -*- coding: utf-8 -*-
from rest_framework.views import APIView, Response
from rest_framework import status
from django.db.models import Q
from django.db.utils import IntegrityError
from src.serializers.exam_registrantion import ExamUserSubjecterializer, InformationStudentExam
from src.models.user import ExamUserSubject, RoomSeat, Information, User, ExamRoomSubject, Room


class ExamRegistrantion(APIView):

    def get(self, request):
        # get  cavschdule
        a = ExamUserSubject.objects.filter(Q(be_register=True) & Q(user_id=10) & Q(exam_id=1))
        b = ExamUserSubjecterializer(a, many=True)
        # //
        c = ExamUserSubject.objects.filter(Q(user_id=10) & Q(status=False))
        d = ExamUserSubjecterializer(c, many=True)
        return Response({"success": True, 'schedule': b.data,})
    def post(self, request):

        information_student_exam = InformationStudentExam(data={'user_id':10,"schedule_id":request.data['schedule_id']})
        if information_student_exam.is_valid():
            try:
              information_student_exam.save()

              return Response({"success": True,"message":"Đăng kí thành công"})
            except IntegrityError:
                return Response({"success": False, "message": "Bản ghi đã tồn tại"})
        else:
            return Response({"success": False,"message":information_student_exam.errors})




    def delete(self, request,id):
        # sua so hoc sinh
        # data{user_id :,schdeule_id , infomattio_id}
        # schedule = ExamRoomSubject.objects.get(pk=2)
        # schedule.no_of_student = schedule.no_of_student - 1
        # schedule.save()
        # # // xoa ban ghi
        # b = Information.objects.get(Q(user=1) & Q(schedule=schedule.id))
        # b.delete()
        # # // sua trang thai mon hoc
        # student_schedule = ExamUserSubject.objects.get(Q(user_id=1) & Q(subject_id=schedule.subject_id))
        # student_schedule.status = True
        # student_schedule.save()
        print(id)
        information_student_exam = InformationStudentExam(data={"user_id":10,"schedule_id":id},)
        if information_student_exam.is_valid():
            information_student_exam.delete()
            return Response({"success": True, "message": "Hủy đăng kí thành công"})


        return Response({"success": True})
