import datetime

from django.db import models

from .exam import Exam
from .room import Room
from .subject import Subject


class ExamRoomSubject(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    day = models.DateField(default=datetime.date.today)
    time_start = models.TimeField(auto_now=False)
    time_end = models.TimeField(auto_now=False)
    no_of_student = models.IntegerField(default=0)
