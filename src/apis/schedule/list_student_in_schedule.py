from rest_framework.views import APIView, Response
from rest_framework import status
from src.serializers.schedule import ScheduleSerializer, ScheduleCreateSerializer
from src.models.user import Information
from src.serializers.ListStudentInSchedule import ListStudentInScheduleSerializer
from django.db.utils import IntegrityError



class ListStudentInScheduleAPI(APIView):
      def get(self, request, id=None):
          print(id)
          try:
              listUser = Information.objects.select_related('user').filter(schedule_id=id)
             # print(len(listUser))
             # data=[]
             # for i in listUser:
             #  data.append({'code':i.user.code,'full_name':i.user.full_name})
              a = ListStudentInScheduleSerializer(listUser,many=True)
              return Response({"success": True, "data": a.data})
          except Exception as e:
              print(e)
              return Response({"success": False, "message": "Co loi xay ra"})



