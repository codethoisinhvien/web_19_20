from  rest_framework import  serializers
from  src.models.user import Room,Seat,RoomSeat
from  django.contrib.auth import hashers

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','name',)
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ('id','name',)
class RoomSeatSerializer(serializers.ModelSerializer):
    room = serializers.SerializerMethodField('get_room')
    seat = serializers.SerializerMethodField('get_seat')
    class Meta:

        model = RoomSeat
        fields = ('room','seat')
    def get_room(self,obj):
        print(obj,"12312")
        return 1 #{"id":obj.room_id.id,"name":obj.room_id.name}

    def get_seat(self, obj):
            return 1


