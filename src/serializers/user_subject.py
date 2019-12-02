from  rest_framework import  serializers
from  src.models.user import ExamUserSubject,Exam,Subject,User
from  django.contrib.auth import hashers

class ExamUserSubjecSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamUserSubject
        fields = '__all__'
    def save_allowed_user(self, **kwargs):
        exam_id = Exam.objects.get(pk=1);
        subject_id = Subject.objects.get(pk=1)
        user_id = User.objects.get(pk=1)
        be_register = True
        allowed_user= ExamUserSubject(exam_id=exam_id,subject_id=subject_id,user_id=user_id,be_register=be_register)
        allowed_user.save()

    def update(self,id,be_register):
        exam_user_subject = ExamUserSubject.objects.get(pk=id)
        exam_user_subject.be_register= be_register
        exam_user_subject.save()
