# -*- coding: utf-8 -*-
from rest_framework.views import APIView, Response

from src.commons.authentication import JsonWebTokenAuthentication
from src.commons.permission import IsAdmin
from src.models import Exam
from src.serializers.exam import ExamSerializer


class ExamAPI(APIView):
    authentication_classes = [JsonWebTokenAuthentication]
    permission_classes = [IsAdmin]

    def put(self, request, id=None):
        print(id)
        exam = Exam.objects.get(id=id)
        exam_serializer = ExamSerializer(data=request.data);
        if exam_serializer.is_valid():
            exam_serializer.update(exam, exam_serializer.validated_data)
            return Response(
                {'success': True, "message": "Sửa kì thi thành công "})
        else:
            return Response({'success': False, "message": "Sửa kì thi thất bại", "error": exam_serializer.errors})

    def delete(self, request, id=None):
        try:
            exam = Exam.objects.get(id=id)
            exam.delete()
            return Response({'success': True, "message": "Xóa kì thi thành công"})
        except Exception as e:
            print(e)
            return Response({'success': True, "message": "Xóa kì thi thành công", "erro": e})
