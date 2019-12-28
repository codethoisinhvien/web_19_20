from rest_framework.views import APIView, Response

from src.models import Room
from src.serializers.room import RoomSerializer
from src.commons.authentication import JsonWebTokenAuthentication
from src.commons.permission import IsAdmin

class ListRoomAPI(APIView):
    authentication_classes = [JsonWebTokenAuthentication]
    permission_classes = [IsAdmin]
    def get(self, request):
        rooms = Room.objects.all()[:10]
        room_serializer = RoomSerializer(rooms, many=True)
        return Response({"success": True, "rooms": room_serializer.data})
