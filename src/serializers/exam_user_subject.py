from rest_framework import serializers

from src.models import ExamUserSubject


class ExamUserSubjectInforSerializer(serializers.ModelSerializer):
    code = serializers.SerializerMethodField('get_code')
    full_name = serializers.SerializerMethodField('get_full_name')
    subject = serializers.SerializerMethodField('get_subject')
    exam = serializers.SerializerMethodField('get_exam')

    class Meta:
        model = ExamUserSubject
        fields = ('code', 'full_name', 'subject','exam','be_register','id')

    def get_code(self, obj):
        return obj.user_id.code

    def get_full_name(self, obj):
        return obj.user_id.full_name

    def get_subject(self, obj):
        return obj.subject_id.name

    def get_exam(self, obj):
        return obj.exam_id.name
