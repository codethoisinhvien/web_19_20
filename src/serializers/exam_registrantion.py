from django.db import connection, transaction
from django.db.models import Q
from rest_framework import serializers

from src.models import ExamUserSubject, ExamRoomSubject
from .schedule import ScheduleSubSerializer
from .subject import SubjectSerializer


class ExamUserSubjecterializer(serializers.ModelSerializer):
    subject_id = serializers.SerializerMethodField('get_subject')
    shift = serializers.SerializerMethodField('get_schedule_subject')
    exam = serializers.SerializerMethodField('get_exam')
    class Meta:
        model = ExamUserSubject
        fields = '__all__'

    def get_subject(self, obj):
        return SubjectSerializer(obj.subject_id).data

    def get_schedule_subject(self, obj):
        data = ExamRoomSubject.objects.filter(Q(subject_id=obj.subject_id.id))
        return ScheduleSubSerializer(data, many=True).data

    def get_exam(self, obj):
        return obj.exam_id.name

class InformationStudentExam(serializers.Serializer):
    schedule_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    class Meta:
        fields = ('schedule_id', "user_id")

    def save(self, **kwargs):
        # tạo giao dịch
        print(self.validated_data['schedule_id'])

        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    # Tăng số học viên lên

                    cursor.execute(
                        "Select exam_id_id,subject_id_id,room_id_id from src_examroomsubject INNER JOIN src_exam ON src_examroomsubject.exam_id_id=src_exam.id where src_examroomsubject.id =%s and src_exam.status = %s",

                        [self.validated_data['schedule_id'], 1])

                    row = cursor.fetchone()
                    # kiem tra sinh vien co thuco ki thi va mon h
                    cursor.execute(
                        "SELECT * FROM `src_examusersubject` WHERE exam_id_id=%s and subject_id_id=%s and user_id_id=%s and status=1",
                        [row[0], row[1], self.validated_data['user_id']])

                    if (cursor.fetchone() is None):
                        raise Exception("Truy cập trái phép")
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
                    print(cursor)

        except Exception as e:
            print(e)
            transaction.rollback(True)
            # raise e

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
