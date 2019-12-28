from rest_framework import serializers

from src.models import Information
from src.serializers.schedule import ScheduleSerializer


class StudentSerializer(serializers.ModelSerializer):
    schedule = serializers.SerializerMethodField('get_schedule')
    seat = serializers.SerializerMethodField('get_seat')

    class Meta:
        model = Information
        fields = ('seat', 'schedule', 'id')

    def get_schedule(self, obj):
        print(obj)
        return ScheduleSerializer(obj.schedule).data

    def get_seat(self, obj):
        print(obj)
        return obj.seat_room_id.seat_id.name
