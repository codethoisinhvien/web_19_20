from django.db import models

from .room import Room
from .seat import Seat
class RoomSeat(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("room_id", "seat_id"))
