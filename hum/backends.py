from hum.models import User
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password


from django.contrib.auth import get_user_model
User = get_user_model()

class AuthBackend(BaseBackend):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False


    def get_user(self, user_id):
       try:
          return User.objects.get(pk=user_id)
       except User.DoesNotExist:
          return None

    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(
                Q(username=username) | Q(email=username) | Q(phone=username)
            )
        except User.DoesNotExist:
            return None

        return user if user.check_password(password) else None


    # def authenticate(self, request, username=None, password=None):
    #     login_valid = (settings.ADMIN_LOGIN == username)
    #     pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
    #     if login_valid and pwd_valid:
    #         try:
    #             user = User.objects.get(username=username)
    #         except User.DoesNotExist:
    #             # Create a new user. There's no need to set a password
    #             # because only the password from settings.py is checked.
    #             user = User(username=username)
    #             user.is_staff = True
    #             user.is_superuser = True
    #             user.save()
    #         return user
    #     return None



# class AuthBackend(object):
#     supports_object_permissions = True
#     supports_anonymous_user = False
#     supports_inactive_user = False


#     def get_user(self, user_id):
#        try:
#           return User.objects.get(pk=user_id)
#        except User.DoesNotExist:
#           return None


#     def authenticate(self, username, password):
#         try:
#             user = User.objects.get(
#                 Q(username=username) | Q(email=username) | Q(phone=username)
#             )
#         except User.DoesNotExist:
#             return None

#         return user if user.check_password(password) else None


    # def authenticate(self, request,username, password):
    #     try:
    #         user = User.objects.get(
    #             Q(username=username) | Q(email=username) | Q(phone=username)
    #         )
    #     except User.DoesNotExist:
    #         return None

    #     return user if user.check_password(password) else None