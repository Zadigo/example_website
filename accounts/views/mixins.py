from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class MessagesMixin:
    base_message = {
        'message': None,
        'level': messages.SUCCESS,
        'extra_tags': 'alert-success'
    }

    FAILED_LOGIN = _('Email or password are not correct')
    FAILED_SIGNUP = _('An error occured')
    EMAIL_NOT_EXISTS = None

    def add_message(self, request, message):
        self.base_message.update(message=message)
        return messages.add_message(request, **self.base_message)
    
    def get_fail_message(self, request, message):
        self.base_message.update(level=messages.WARNING, extra_tags='alert-danger')
        self.add_message(request, message)

    def get_success_message(self, request, message):
        self.add_message(request, message)

    def failed_login_message(self, request):
        self.add_message(request, self.FAILED_LOGIN)


class ProfileMixin:
    queryset = None

    def get_context_data(self, request, **kwargs) -> dict:
        context = super().get_context_data()
        user, profile = self.get_user()
        context.update({'user': user, 'profile': profile})
        return context

    def get_user(self, request, **kwargs):
        return request.user, request.user.myuserprofile
