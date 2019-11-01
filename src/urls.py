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

from django.urls import path
from src.apis.user.user_authentication import UserAuthentication
from src.apis.user.user import User
from src.apis.user.list_user import ListUser
from .apis.exam.exam import ExamAPI
from src.apis.exam.list_exam import ListExamAPI
from django.conf.urls import url
from src.apis.schedule.schedule import ScheduleAPI
from src.apis.exam.exam_registration import  ExamRegistrantion
from src.apis.subject.list_subject import  ListSubjectAPI
from src.apis.list_room import ListRoomAPI
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [

  url(r'authentication',UserAuthentication.as_view(),name='login'),
  url(r'user/',User.as_view(),name='user'),
  url(r'users/',ListUser.as_view(),name='users'),
  path(r'exam/<int:id>/', ExamAPI.as_view(), name='exam'),
  url(r'exams/', ListExamAPI.as_view(), name='list_exam'),

  path(r'exam-resgister/<int:id>', ExamRegistrantion.as_view(), name='exam-resgister'),

  url(r'exam-resgister/', ExamRegistrantion.as_view(), name='exams-resgister'),
  path(r'schedules/', ScheduleAPI.as_view(), name='schedule'),
  path(r'schedules/<int:id>', ScheduleAPI.as_view(), name='schedule'),
  path(r'subjects/', ListSubjectAPI.as_view(), name='list-subject'),
  path(r'subject/<int:id>', ExamRegistrantion.as_view(), name='subject'),
  path(r'rooms/', ListRoomAPI.as_view(), name='list-room')
]
urlpatterns = format_suffix_patterns(urlpatterns)