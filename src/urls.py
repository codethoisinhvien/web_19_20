"""ExamReg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from src.apis.exam.exam_registration import ExamRegistrantion
from src.apis.exam.list_exam import ListExamAPI
from src.apis.list_room import ListRoomAPI
from src.apis.schedule.list_student_in_schedule import ListStudentInScheduleAPI
from src.apis.schedule.schedule import ScheduleAPI
from src.apis.subject.list_subject import ListSubjectAPI
from src.apis.subject.subject import SubjectAPI
from src.apis.user.list_student_in_subject import ListUserInSubjectApi
from src.apis.user.list_user import ListUser
from src.apis.user.user import UserApi
from src.apis.user.user_authentication import UserAuthentication
from src.apis.user.user_in_subject import UserInSubjectApi
from .apis.exam.exam import ExamAPI
from .apis.exam.student_register import StudentRegistrantion

urlpatterns = [
    path(r'authentication', UserAuthentication.as_view(), name='login'),
    path(r'users/', ListUser.as_view(), name='users'),
    path(r'users/<int:id>', UserApi.as_view(), name='user'),
    path(r'subjects/user', ListUserInSubjectApi.as_view(), name='user-subject'),
    path(r'subjects/user/<int:id>', UserInSubjectApi.as_view(), name='user-subject'),
    path(r'schedules/<int:id>/users', ListStudentInScheduleAPI.as_view(), name='exam-resgister'),
    path(r'subjects/', ListSubjectAPI.as_view(), name='list-subject'),
    path(r'subjects/<int:id>', SubjectAPI.as_view(), name='subject'),
    path(r'exams/', ListExamAPI.as_view(), name='list_exam'),
    path(r'exams/<int:id>', ExamAPI.as_view(), name='exam'),
    path(r'schedules/', ScheduleAPI.as_view(), name='schedule'),
    path(r'schedules/<int:id>', ScheduleAPI.as_view(), name='schedule'),
    path(r'rooms/', ListRoomAPI.as_view(), name='list-room'),
    path(r'user/', UserApi.as_view(), name='user'),
    path(r'exam-resgister/', ExamRegistrantion.as_view(), name='exams-resgister'),
    path(r'exam-resgister/<int:id>', ExamRegistrantion.as_view(), name='exam-resgister'),
    path(r'student-resgister/',StudentRegistrantion.as_view(), name='exam-resgister'),







]
urlpatterns = format_suffix_patterns(urlpatterns)
