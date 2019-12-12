# -*- coding: utf-8 -*-
from rest_framework.views import APIView, Response

from src.models.user import Information
from src.serializers.student_register import StudentSerializer

class StudentRegistrantion(APIView):

    def get(self, request):
        c = Information.objects.select_related('schedule').filter(user=10)
        d = StudentSerializer(c, many=True)
        print(d.data)
        return Response({"success": True, 'schedules':d.data })
