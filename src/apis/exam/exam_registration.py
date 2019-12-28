# -*- coding: utf-8 -*-

from django.db.models import Q
from django.db.utils import IntegrityError
from rest_framework.views import APIView, Response

from src.commons.authentication import JsonWebTokenAuthentication
from src.commons.permission import IsStudent
from src.models import ExamUserSubject
from src.serializers.exam_registrantion import ExamUserSubjecterializer, InformationStudentExam


class ExamRegistrantion(APIView):
    authentication_classes = [JsonWebTokenAuthentication]
    permission_classes = [IsStudent]

    def get(self, request):
        # get  cavschdule

        user_id = request.user['id']
        try:
            query = ExamUserSubject.objects.select_related('exam_id').filter(
                Q(be_register=True) & Q(user_id=user_id) & Q(exam_id__status=True))
            data = ExamUserSubjecterializer(query, many=True)
            return Response({"success": True, 'schedule': data.data, })
        except:
            return Response({"success": False, 'message': "Có lỗi xảy ra"})

    def post(self, request):
        user_id = request.user['id']
        information_student_exam = InformationStudentExam(
            data={'user_id': user_id, "schedule_id": request.data['schedule_id']})
        if information_student_exam.is_valid():
            try:
                information_student_exam.save()

                return Response({"success": True, "message": "Đăng kí thành công"})
            except IntegrityError:
                return Response({"success": False, "message": "Bản ghi đã tồn tại"})
            except Exception as e:
                print(e)
                return Response({"success": False, "message": "Đã có lỗi xảy ra"})
        else:
            return Response({"success": False, "message": information_student_exam.errors})

    def delete(self, request, id):
        try:
            user_id = request.user['id']
            information_student_exam = InformationStudentExam(data={"user_id": user_id, "schedule_id": id}, )
            if information_student_exam.is_valid():
                information_student_exam.delete()
                return Response({"success": True, "message": "Hủy đăng kí thành công"})
            raise Exception("CÓ lỗi xảy ra")
        except:

            return Response({"success": False, "message": "Có lỗi xảy ra"})
