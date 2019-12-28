from rest_framework.views import APIView, Response

from src.models import Information
from src.serializers.list_student_in_schedule import ListStudentInScheduleSerializer
from src.commons.authentication import JsonWebTokenAuthentication
from src.commons.permission import IsAdmin
class ListStudentInScheduleAPI(APIView):
    authentication_classes = [JsonWebTokenAuthentication]
    permission_classes = [IsAdmin]
    def get(self, request, id=None):

        try:
            listUser = Information.objects.select_related('user').filter(schedule_id=id)
            data = ListStudentInScheduleSerializer(listUser, many=True)
            return Response({"success": True, "data": data.data})
        except Exception as e:
            print(e)
            return Response({"success": False, "message": "Co loi xay ra"})
