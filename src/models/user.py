from django.db import models
import datetime
class User(models.Model):
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    role = models.IntegerField(default=1)



class Exam(models.Model):
    name = models.CharField(max_length=255,unique=True)
    status = models.BooleanField(default=False)

class Room(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    max_student = models.IntegerField()
class Subject(models.Model):
    name = models.CharField(max_length=255,null=False);
    code = models.CharField(max_length=255,unique=True,)
class Seat (models.Model):
    name = models.CharField(max_length=255)

class ExamRoomSubject(models.Model):
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room,on_delete=models.CASCADE)
    exam_id = models.ForeignKey(Exam,on_delete=models.CASCADE)
    day =  models.DateField(default=datetime.date.today)
    time_start= models.TimeField(auto_now=False)
    time_end  = models.TimeField(auto_now=False)
    no_of_student = models.IntegerField(default=0)

class ExamUserSubject(models.Model):
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    exam_id = models.ForeignKey(Exam,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    be_register = models.BooleanField(default=True)
    class Meta:
      unique_together = (("subject_id","user_id","exam_id"))
class RoomSeat(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    class Meta:
      unique_together = (("room_id", "seat_id"))
class Information(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE,default ="")
    schedule = models.ForeignKey(ExamRoomSubject,on_delete=models.CASCADE,default="")
    seat_room_id= models.ForeignKey(RoomSeat, on_delete=models.CASCADE)

    class Meta:

        unique_together = (("user", "schedule"))
