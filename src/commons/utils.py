from datetime import datetime

import jwt
from rest_framework_jwt.settings import api_settings

from src.models import ExamRoomSubject


def jwt_payload_handler(user):
    payload = jwt.decode(user, "123456", algorithm='HS256')
    return payload


def jwt_encode_handler(payload):
    payload['exp'] = datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    return jwt.encode(payload, "123456", algorithm='HS256')


def check_schedule_in_room(room_id, day, time_start, time_end):
    list_schedule = ExamRoomSubject.objects.filter(room_id__id=room_id, day=day).order_by('time_start')

    list_time = [(i.time_start, i.time_end) for i in list_schedule]
    print(list_time)
    print("dsdas", datetime.strptime(time_start, '%H:%M').time())
    check_schedule(list_time,
                   (datetime.strptime(time_start, '%H:%M').time(), datetime.strptime(time_end, '%H:%M').time()))
    print(list_schedule)
    return True


def check_schedule(list_time, time_schedule):
    check = False
    check_hight = True
    # kiểm tra đúng đắn trong  khung giờ
    if time_schedule[0] >= time_schedule[1]:
        raise "Thông số giờ thi không hợp lệ"
    length = len(list_time)
    if length == 0:
        return True
    for i in range(length):
        if (i == 0):
            if time_schedule[1] < list_time[i][0]:
                return True
        elif (i == length - 1):
            if time_schedule[0] > list_time[i][1]:
                return True
        else:
            check = time_schedule[0] > list_time[i - 1][1] & time_schedule[1] < time_schedule[i][0]
            if check == True:
                return True

    raise "Lịch thi bị trùng"
    return False
