from calendar import timegm
from datetime import datetime
import jwt
from rest_framework_jwt.compat import get_username_field
from rest_framework_jwt.settings import api_settings


def jwt_payload_handler(user):


    return  jwt.decode(user,"123456", algorithm='HS256')
def jwt_encode_handler(payload):
    payload['exp'] = datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    return jwt.encode(payload,"123456", algorithm='HS256')
