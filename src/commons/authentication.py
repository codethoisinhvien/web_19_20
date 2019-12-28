from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import BasePermission
from rest_framework import HTTP_HEADER_ENCODING, authentication,exceptions
from rest_framework_jwt.settings import api_settings

class JsonWebTokenAuthentication(BasicAuthentication):

     def authenticate(self, request):

         hearder =  self.get_header(request)

         if hearder is None:
             raise  exceptions.AuthenticationFailed('No such user')

         try:
             user = api_settings.JWT_PAYLOAD_HANDLER(hearder)

             return (user, None)
         except Exception as e :
             print(e)
             raise exceptions.AuthenticationFailed('No such user')




     def get_header(self, request):
         """
         Extracts the header containing the JSON web token from the given
         request.
         """
         header = request.META.get('HTTP_AUTHORIZATION')
         if header is None:
             raise exceptions.AuthenticationFailed('No token')
         if isinstance(header, str):
             # Work around django test client oddness

             header= header[7:len(header)]

             header = header.encode(HTTP_HEADER_ENCODING)

         return header

