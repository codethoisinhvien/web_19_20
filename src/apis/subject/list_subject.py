from rest_framework.views import APIView, Response

from src.models import Subject
from src.serializers.subject import SubjectSerializer
from src.commons.permission import IsAdmin
from src.commons.authentication import JsonWebTokenAuthentication
class ListSubjectAPI(APIView):
    authentication_classes = [JsonWebTokenAuthentication]
    permission_classes = [IsAdmin]
    def get(self, request):
        subject_name = request.GET.get('subject')
        if (subject_name is None):
            subject_name = ''
        try:
            subjects = Subject.objects.filter(name__contains=subject_name)
            subject_serializer = SubjectSerializer(subjects, many=True)
            return Response({"success": True, "subjects": subject_serializer.data})
        except Exception as e:
            return Response({"success": False, "message": "Có lỗi xảy ra"})

    def post(self, request):
        subject_serializer = SubjectSerializer(data=request.data)
        if subject_serializer.is_valid():
            try:
                subject_serializer.save()
                return Response({"success": True, "message": "Tạo môn học thành công ",
                                 "subject_id": subject_serializer.data['id']})
            except Exception as e:

                return Response({"success": False, "message": "Tạo môn học thất bại"})
        else:
            return Response({"success": False, "message": "Dữ liệu không hợp lệ hoặc bản ghi đã tồn tại "})
