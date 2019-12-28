from django.db import models

from .exam import Exam
from .subject import Subject
from .user import User


class ExamUserSubject(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    be_register = models.BooleanField(default=True)

    class Meta:
        unique_together = (("subject_id", "user_id", "exam_id"))
