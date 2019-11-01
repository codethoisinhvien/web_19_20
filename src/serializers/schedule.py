from rest_framework import serializers
from src.models.user import ExamRoomSubject, Exam, Room, Subject
from src.serializers.room import RoomSerializer
from django.contrib.auth import hashers
import datetime


class ScheduleSerializer(serializers.ModelSerializer):
    exam = serializers.SerializerMethodField('get_exam')
    room = serializers.SerializerMethodField('get_room')
    subject = serializers.SerializerMethodField('get_subject')
    start_time = serializers.SerializerMethodField('get_start_time')
    end_time = serializers.SerializerMethodField('get_end_time')
    no_of_student = serializers.SerializerMethodField('get_student')
    max_student = serializers.SerializerMethodField('get_max_student')

    class Meta:
        model = ExamRoomSubject
        fields = ('id', 'room', 'exam', 'subject', 'start_time', 'end_time', 'no_of_student', 'max_student', 'day')

    def get_room(self, obj):
        return obj.room_id.name

    def get_exam(self, obj):
        return obj.exam_id.name

    def get_subject(self, obj):
        return obj.subject_id.name

    def get_start_time(self, obj):
        return obj.time_start.strftime('%H:%M:%S')

    def get_end_time(self, obj):
        return obj.time_end.strftime('%H:%M:%S')

    def get_student(self, obj):
        return obj.no_of_student

    def get_max_student(self, obj):
        return obj.room_id.max_student



class ScheduleCreateSerializer(serializers.Serializer):
    exam_id = serializers.IntegerField()
    room_id = serializers.IntegerField()
    subject_id = serializers.IntegerField()
    day = serializers.DateField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()

    def save(self, **kwargs):
        exam_id = Exam.objects.get(pk=self.validated_data['exam_id'])
        room_id = Room.objects.get(pk=self.validated_data['room_id'])
        subject_id = Subject.objects.get(pk=self.validated_data['subject_id'])
        day = datetime.date.today()
        time_start = datetime.datetime.now(),
        time_end = datetime.datetime.now(),
        print(time_start)

        schedule = ExamRoomSubject(
            exam_id=exam_id,
            room_id=room_id,
            subject_id=subject_id,
            day=day,
            time_start=datetime.datetime.now(),
            time_end=datetime.datetime.now()
        )
        schedule.save()

    def update(self, instance):
        print(self.validated_data)
        instance.exam_id = Exam.objects.get(pk=self.validated_data['exam_id'])

        instance.subject_id = Subject.objects.get(pk=self.validated_data['subject_id'])
        instance.room_id = Room.objects.get(pk=self.validated_data['room_id'])
        instance.day = self.validated_data['day']
        instance.time_start = self.validated_data['start_time']
        instance.time_end = self.validated_data['end_time']
        instance.save()


class ScheduleSubSerializer(serializers.ModelSerializer):
    room_id = serializers.SerializerMethodField('get_room')

    class Meta:
        model = ExamRoomSubject
        fields = ('id', 'room_id', 'time_start', 'time_end', 'no_of_student','day')

    def get_room(self, obj):
        return RoomSerializer(obj.room_id).data
