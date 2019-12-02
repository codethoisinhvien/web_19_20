from rest_framework.views import APIView, Response
from rest_framework import status
from src.commons.authentication import IsTest
from rest_framework_jwt.settings import api_settings
from src.serializers.user import UserSerializer
from src.commons.authentication import JsonWebTokenAuthentication
from src.serializers.user_subject import ExamUserSubjecSerializer
from src.models.user import Exam, User, Subject, ExamUserSubject
from django.db.models import Q


class ListUserInSubjectApi(APIView):
    # tạo sinh viên bị cấm thi hoặc không bi cấm thi
    def post(self, request):


        try:
            #data = {"code": "17020708", "subject_code": "INT 3306", "exam_name": "Kì thi học kì 1"}

            exam_id = Exam.objects.get(name=request.data['exam']);
            print(exam_id.name)
            user_id = User.objects.get(code=request.data['code'])
            print(user_id.code)
            subject_id = Subject.objects.get(code=request.data['subject'])
            be_register=request.data['be_register']
        except Exception as e:
            return Response({'success': False, "message": str(e)})
        exam_user_subject = ExamUserSubjecSerializer(
            data={"exam_id": exam_id.id, "subject_id": subject_id.id, "user_id": user_id.id, 'be_register': be_register})
        if exam_user_subject.is_valid():
            try:
                exam_user_subject.save()
                return Response({'success': True, "message": "Đăng kí thành công"})
            except:
                return Response({'success': False, "message": "Lỗi hệ thống"})
        else:
            return Response({'success': False, "message": exam_user_subject.errors})

    def get(self, request):
        return Response({'user': 'giang'})

    def put(self, request):
        try:
            exam_id = Exam.objects.get(name="abc");
            print(exam_id.name)
            user_id = User.objects.get(code="17020708")
            print(user_id.code)
            subject_id = Subject.objects.get(code='INT 3306 1')
            print(subject_id.code
                  )
            exam_user_subject = ExamUserSubject.objects.get(
                Q(subject_id=subject_id.id) & Q(user_id=user_id.id) & Q(exam_id=exam_id.id))

        except Exception as e:
            return Response({'success': False, "message": str(e)})

        try:
            exam_user_subject.status = False
            exam_user_subject.save()
            return Response({'success': True, "message": "Thành công"})
        except Exception as e:
            print(e)
            return Response({'success': False, "message": "Lỗi hệ thống"})

    def delete(self, request):
        pass
