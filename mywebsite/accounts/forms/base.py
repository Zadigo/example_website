from accounts.widgets import EmailInput, PasswordInput, TextInput
from django.contrib.auth import authenticate
from django.forms import Form, ValidationError, fields, widgets
from django.forms.fields import CharField
from django.utils.translation import gettext_lazy as _


class BaseFormMixin(Form):
    token = CharField(max_length=100, required=True)

    def __init__(self, data, **kwargs):
        super().__init__(data=data, **kwargs)


class AuthenticationForm(Form):
    """
    A base form for authenticating users with
    an email and a password
    """
    email = fields.EmailField(
        widget=EmailInput(attrs={'autofocus': True})
    )
    password = fields.CharField(
        label=_('Password'),
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'current-password'})
    )

    error_messages = {
        'invalid_login': _("%(email)s and/or password is not correct"),
        'inactive': _('This account is not active')
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(**kwargs)
        
        self.email_field = 'email'

    def _create_token(self):
        return get_random_string(26 + 26 + 10)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if self.request is not None:
            if email is not None and password:
                self.user_cache = authenticate(self.request, email=email, password=password)
                if self.user_cache is None:
                    raise ValidationError(self.error_messages['invalid_login'], code='invalid_login', params={'email': self.email_field})
                else:
                    # self.confirm_login_allowed(self.user_cache)
                    pass
        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(self.error_messages['inactive'], code='inactive')

    def get_user(self):
        return self.user_cache
