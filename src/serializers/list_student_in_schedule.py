
from rest_framework import serializers
from src.models import Information
class ListStudentInScheduleSerializer(serializers.ModelSerializer):
    code = serializers.SerializerMethodField('get_code')
    full_name = serializers.SerializerMethodField('get_full_name')
    seat = serializers.SerializerMethodField('get_seat')
    class Meta:
        model = Information
        fields = ('code','full_name','seat')

    def get_code(self, obj):
        return obj.user.code

    def get_full_name(self, obj):
        return obj.user.full_name

    def get_seat(self, obj):
        return obj.seat_room_id.seat_id.name


