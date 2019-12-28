from django.db.models import Q
from rest_framework.views import APIView, Response

from src.models import Exam, User, Subject, ExamUserSubject
from src.serializers.exam_user_subject import ExamUserSubjectInforSerializer
from src.serializers.user_subject import ExamUserSubjecSerializer
from src.commons.authentication import JsonWebTokenAuthentication
from src.commons.permission import IsAdmin
class ListUserInSubjectApi(APIView):
    # tạo sinh viên bị cấm thi hoặc không bi cấm thi
    authentication_classes = [JsonWebTokenAuthentication]
    permission_classes = [IsAdmin]
    def post(self, request):

        try:


            exam_id = Exam.objects.get(name=request.data['exam']);

            user_id = User.objects.get(code=request.data['code'])
            subject_id = Subject.objects.get(code=request.data['subject'])
            be_register = request.data['be_register']
        except Exception as e:
            return Response({'success': False, "message": str(e)})
        exam_user_subject = ExamUserSubjecSerializer(
            data={"exam_id": exam_id.id, "subject_id": subject_id.id, "user_id": user_id.id,
                  'be_register': be_register})
        if exam_user_subject.is_valid():
            try:
                exam_user_subject.save()
                return Response({'success': True, "message": "Đăng kí thành công"})
            except:
                return Response({'success': False, "message": "Lỗi hệ thống"})
        else:
            return Response({'success': False, "message": exam_user_subject.errors})

    def get(self, request):
        code = request.GET.get('code')
        subject = request.GET.get('subject')
        exam = request.GET.get('exam')
        print(code, subject, exam)
        examUserSubject = ExamUserSubject.objects \
            .select_related('user_id') \
            .select_related('subject_id') \
            .select_related('exam_id') \
            .filter(user_id__code__contains=code, exam_id__name__contains=exam,
                    subject_id__name__contains=subject)
        data = ExamUserSubjectInforSerializer(examUserSubject, many=True)

        return Response({"success": True, "data": data.data})

    def put(self, request):
        try:
            exam_id = Exam.objects.get(name="abc");
            user_id = User.objects.get(code="17020708")
            subject_id = Subject.objects.get(code='INT 3306 1')
            exam_user_subject = ExamUserSubject.objects.get(
                Q(subject_id=subject_id.id) & Q(user_id=user_id.id) & Q(exam_id=exam_id.id))

        except Exception as e:
            return Response({'success': False, "message": str(e)})

        try:
            exam_user_subject.status = False
            exam_user_subject.save()
            return Response({'success': True, "message": "Thành công"})
        except Exception as e:
            return Response({'success': False, "message": "Lỗi hệ thống"})

    def delete(self, request):
        pass
