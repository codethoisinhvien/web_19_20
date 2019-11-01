from rest_framework.views import APIView, Response
from rest_framework import status
from src.serializers.subject import SubjectSerializer
from src.models.user import Subject
from django.db.utils import IntegrityError



class SubjectAPI(APIView):
    def get(self,request):
        subjects =Subject.objects.all()[:10]
        subject_serializer = SubjectSerializer(subjects,many=True)
        return Response({"success":True,"subjects":subject_serializer.data})
    def post(self,request):
        data = {"code":"INT 3306 1","name":"Lập trình hướng đới tượng"}
        subject_serializer= SubjectSerializer(data=request.data)
        if subject_serializer.is_valid():
            try:
             subject_serializer.save()
             return Response({"success": True, "message": "Tạo môn học thành công "})
            except Exception as e :

              return  Response({"success":False,"message":"Tạo môn học thất bại"})
        else:
            return Response({"success": False, "message": "Dữ liệu không hợp lệ hoặc bản ghi đã tồn tại "})
