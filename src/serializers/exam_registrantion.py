from rest_framework import serializers
from src.models.user import ExamUserSubject, Subject, RoomSeat, Information, ExamRoomSubject
from .subject import SubjectSerializer
from .schedule import ScheduleSubSerializer
from django.db.models import Q, Subquery
from django.db import connection, transaction


class ExamUserSubjecterializer(serializers.ModelSerializer):
    subject_id = serializers.SerializerMethodField('get_subject')
    shift = serializers.SerializerMethodField('get_schedule_subject')

    class Meta:
        model = ExamUserSubject
        fields = '__all__'

    def get_subject(self, obj):
        return SubjectSerializer(obj.subject_id).data

    def get_schedule_subject(self, obj):
        b = ExamRoomSubject.objects.filter(Q(subject_id=obj.subject_id.id), )
        return ScheduleSubSerializer(b, many=True).data


class InformationStudentExam(serializers.Serializer):
    schedule_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    class Meta:
        fields = ('schedule_id', "user_id")

    def save(self, **kwargs):
        # tạo giao dịch
        print(self.validated_data['schedule_id'])
        with transaction.atomic():
            with connection.cursor() as cursor:
                try:
                    cursor.execute(
                        "Select exam_id_id,subject_id_id,room_id_id from src_examroomsubject  where id =%s",
                        [self.validated_data['schedule_id']])

                    row = cursor.fetchone()
                    # Thay đổi trạng thái có thể đăng kí môn của 1 môn học trong 1 kì thi
                    cursor.execute(
                        "UPDATE src_examusersubject SET status = 0 WHERE user_id_id = %s and exam_id_id = %s and subject_id_id =%s",
                        [self.validated_data['user_id'], row[0], row[1]])
                    # Tăng số học viên lên
                    cursor.execute(
                        "UPDATE src_examroomsubject SET no_of_student = no_of_student+1 WHERE id = %s",
                        [self.validated_data['schedule_id']])
                    # tìm kiếm ghế trống
                    cursor.execute(
                        "Select id from src_roomseat  where id not in ( select seat_room_id_id from src_information where schedule_id = %s )  and room_id_id = %s limit 1",
                        [self.validated_data['schedule_id'], row[2]])
                    seat_room_id = cursor.fetchone()
                    # thêm bản ghi  vào bảng
                    cursor.execute(
                        "INSERT  into src_information (schedule_id,user_id,seat_room_id_id) VALUES( %s , %s,%s )",
                        [self.validated_data['schedule_id'], self.validated_data['user_id'], seat_room_id])
                    # thiết kế giải quyết được kiểm tả 1 người không thể đăng kí 2 lịch
                except Exception as e:
                    transaction.set_rollback(True)
                    raise e

    def delete(self, ):
        with transaction.atomic():
            try:
                with connection.cursor() as cursor:
                    cursor.execute("select id  from  src_information where schedule_id=%s and  user_id =%s",
                                   [self.validated_data['schedule_id'], self.validated_data['user_id']])
                    if cursor.fetchone() is None:
                        raise Exception("Dữ liệu không tồn tại")
                    # xóa bản ghi (shedule_id,user_id)
                    cursor.execute("delete  from  src_information where schedule_id=%s and  user_id =%s",
                                   [self.validated_data['schedule_id'], self.validated_data['user_id']])
                    # thay đổi số học viên(schedule_id)
                    cursor.execute("SELECT exam_id_id,subject_id_id FROM src_examroomsubject WHERE id =%s",
                                   [self.validated_data['schedule_id']])
                    row = cursor.fetchone()
                    cursor.execute(
                        "UPDATE src_examroomsubject SET no_of_student = no_of_student-1 WHERE id = %s",
                        [self.validated_data['schedule_id']])
                    # Thay đổi trang thái(user_id,subject_id,exam_id)
                    cursor.execute(
                        "UPDATE src_examusersubject SET status = 1 WHERE user_id_id=%s and subject_id_id =%s and exam_id_id = %s",
                        [self.validated_data['user_id'], row[1], row[0]])
            except Exception as e:
                transaction.rollback(True)
                raise e
