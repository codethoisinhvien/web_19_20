from django.db import models

from .exam_room_subject import ExamRoomSubject
from .room_seat import RoomSeat
from .user import User


class Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    schedule = models.ForeignKey(ExamRoomSubject, on_delete=models.CASCADE, default="")
    seat_room_id = models.ForeignKey(RoomSeat, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "schedule"))
