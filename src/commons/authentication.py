from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import BasePermission
from rest_framework import HTTP_HEADER_ENCODING, authentication,exceptions
from rest_framework_jwt.settings import api_settings
class IsTest(BasePermission):
     message = "anh"
     def has_permission(self, request, view):
         return  True
     def has_object_permission(self, request, view, obj):
         return False


class IsTest2(BasePermission):
    message = "anh"

    def has_permission(self, request, view):
        return True
class JsonWebTokenAuthentication(BasicAuthentication):

     def authenticate(self, request):

         hearder =  self.get_header(request)
         print(hearder,"fsf")
         if hearder is None:
             pass


         user = api_settings.JWT_PAYLOAD_HANDLER(hearder)
         print(user)
         raise  exceptions.AuthenticationFailed('No such user')
         #return (user, None)

     def get_header(self, request):
         """
         Extracts the header containing the JSON web token from the given
         request.
         """
         header = request.META.get('HTTP_AUTHORIZATION')

         if isinstance(header, str):
             # Work around django test client oddness
             header = header.encode(HTTP_HEADER_ENCODING)

         return header

