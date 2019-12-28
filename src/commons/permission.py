from rest_framework.permissions import BasePermission
from rest_framework import HTTP_HEADER_ENCODING, authentication,exceptions
from rest_framework_jwt.settings import api_settings
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        hearder = self.get_header(request)

        if hearder is None:
            return False

        try:
            user = api_settings.JWT_PAYLOAD_HANDLER(hearder)
            print(user['role']==2)
            if (user['role']==2):
                return True
            return False

        except Exception as e:
            print(e)
            return  False

    def get_header(self, request):
         """
         Extracts the header containing the JSON web token from the given
         request.
         """
         header = request.META.get('HTTP_AUTHORIZATION')

         if isinstance(header, str):
             # Work around django test client oddness
             header = header[7:len(header)]
             header = header.encode(HTTP_HEADER_ENCODING)


         return header
class IsStudent(BasePermission):
    message = "anh"

    def has_permission(self, request, view):
        hearder = self.get_header(request)

        if hearder is None:
            return False

        try:
            user = api_settings.JWT_PAYLOAD_HANDLER(hearder)
            print(user['role']==1)
            if (user['role']==1):
                return True
            return False

        except Exception as e:
            print(e)
            return  False

    def get_header(self, request):
         """
         Extracts the header containing the JSON web token from the given
         request.
         """
         header = request.META.get('HTTP_AUTHORIZATION')

         if isinstance(header, str):
             # Work around django test client oddness
             header = header[7:len(header)]
             header = header.encode(HTTP_HEADER_ENCODING)


         return header
