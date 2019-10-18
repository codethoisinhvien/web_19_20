from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=256)
    role = models.IntegerField(default=1)
class Exam(models.Model):
    name = models.TextField()

class Room(models.Model):
    name = models.IntegerField()
    location = models.TextField()
    max_student = models.IntegerField()
class Subject(models.Model):
    name = models.TextField()
class ExamSubjectAssignment(models.Model):
    exam_id = models.ForeignKey(Exam,on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()


class SubjectRoomAssignment(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    rom_id     = models.ForeignKey(Room, on_delete=models.CASCADE)

class UserSubject(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
class OrderDetail(models.Model):
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    rom_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.IntegerField()
    be_registered = models.BooleanField()

