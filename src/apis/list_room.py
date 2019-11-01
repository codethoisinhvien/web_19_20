from rest_framework.views import APIView, Response
from rest_framework import status
from src.serializers.room import RoomSerializer
from src.models.user import Room
from django.db.utils import IntegrityError

class ListRoomAPI(APIView):
    def get(self,request):
        rooms =Room.objects.all()[:10]
        room_serializer = RoomSerializer(rooms,many=True)
        return Response({"success":True,"rooms":room_serializer.data})
