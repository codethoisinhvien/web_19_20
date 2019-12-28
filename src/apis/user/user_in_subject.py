from rest_framework.views import APIView, Response

from src.models import ExamUserSubject

from src.commons.authentication import JsonWebTokenAuthentication
from src.commons.permission import IsAdmin
class UserInSubjectApi(APIView):
    # sua thong tin của sinh vien trong 1 mon thi
    authentication_classes = [JsonWebTokenAuthentication]
    permission_classes = [IsAdmin]
    def patch(self, request, id):
        try:
            user_subject = ExamUserSubject.objects.get(pk=id);
            user_subject.be_register = request.data['be_register']
            user_subject.save()
            return Response({'success': True, "message": "Thay đổi thành công"})
        except Exception as e:
            print(e)
        return Response({'success': True, "message": "Thay đổi thất bại"})

    # xóa thi sinh 1 môn thi
    def delete(self, request, id):
        try:
            user_subject = ExamUserSubject.objects.get(pk=id)
            user_subject.delete()
            return Response({'success': True, "message": "Xóa thành công"})
        except Exception as e:
            print(e)
            return Response({'success': False, "message": "Xóa thất bại "})
