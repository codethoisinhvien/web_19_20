# -*- coding: utf-8 -*-
from django.db.models import Q
from rest_framework.views import APIView, Response

from src.commons.authentication import JsonWebTokenAuthentication
from src.commons.permission import IsStudent
from src.models import Information
from src.serializers.student_register import StudentSerializer

from src.commons.authentication import JsonWebTokenAuthentication
class StudentRegistrantion(APIView):
    # dang sach sinh vien trong 1 ca thi
    authentication_classes = [JsonWebTokenAuthentication]
    permission_classes = [IsStudent]

    def get(self, request):

        try:
            user_id = request.user['id']
            condition = Q(user=user_id)
            exam_name = request.GET.get('exam')
            if (exam_name is not None):
                condition = condition & Q(schedule__exam_id__name__contains=exam_name)
            else:
                condition = condition & Q(schedule__exam_id__status=True)
            list_schedule = Information.objects.select_related('schedule') \
                .filter(condition)
            data = StudentSerializer(list_schedule, many=True)
            return Response({"success": True, 'schedules': data.data})
        except Exception as e:
            print(e)
            return Response({"success": False, 'schedules': "Có lỗi xảy ra"})
