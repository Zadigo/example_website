from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

USER_MODEL = get_user_model()

class EmailAuthenticationBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = USER_MODEL.objects.get(email=email)
        except USER_MODEL.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        try:
            user = USER_MODEL.objects.get(pk=user_id)
        except USER_MODEL.DoesNotExist:
            user = None
        else:
            return user if self.user_can_authenticate(user) else None
