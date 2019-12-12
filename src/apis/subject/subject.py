from rest_framework.views import APIView, Response

from src.models.user import Subject
from src.serializers.subject import SubjectSerializer


class SubjectAPI(APIView):

    def put(self, request, id):
        data = {"code": "INT 3306 1", "name": "Lập trình hướng đới tượng"}
        subject_serializer = SubjectSerializer(data=request.data)
        if subject_serializer.is_valid():
            try:
                subject = Subject.objects.get(pk=id)
                subject_serializer.update(subject, subject_serializer.validated_data)
                return Response({"success": True, "message": "Sửa  môn học thành công "})
            except Exception as e:
                print(e)
                return Response({"success": False, "message": "Sửa môn học thất bại"})
        else:
            print(subject_serializer.errors)
            return Response({"success": False, "message": "Dữ liệu không hợp lệ hoặc bản ghi đã tồn tại "})

    def delete(self, request, id):
        try:
            subject = Subject.objects.get(pk=id);
            subject.delete()
            return Response({"success": True, "message": "Xóa môn thi thành công"})
        except Exception as e:
            print(e)
            return Response({"success": False, "message": "Xóa môn thi thất bại"})
