from accounts.forms.base import AuthenticationForm
from accounts.models import MyUser
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError, fields, widgets
from django.urls.base import reverse_lazy
from django.utils.crypto import get_random_string, salted_hmac
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _

USER_MODEL = get_user_model()

class UserLoginForm(AuthenticationForm):
    """A base form for login users"""
    error_messages = {
        'invalid_login': _("%(email)s and/or password is not correct"),
        'inactive': _(mark_safe("This account is not active <a href='/accounts/activate/send'>"
        "send activation link</a>"))
    }


class UserSignupForm(UserCreationForm):
    password1 = fields.CharField(
        widget=widgets.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password', 'placeholder': 'Mot de passe'}),
        strip=False,
    )
    password2 = fields.CharField(
        widget=widgets.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password', 'placeholder': 'Confirmation du mot de passe'}),
        strip=False
    )

    class Meta:
        fields = ['firstname', 'lastname', 'email']
        model = MyUser
        widgets = {
            'firstname': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'lastname': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1:
            raise ValidationError(_('Veuillez entrer un mot de passe'))
        
        if password1 != password2:
            raise ValidationError(_('Les mots de passe ne correspondent pas'))

        if len(password1) < 10:
            raise ValidationError(_('Votre mot de passe doit comporter au moins 10 charactères'))
        
        validate_password(password2)
        return self.cleaned_data


class SendActivationEmailForm(forms.Form):
    email = fields.EmailField()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_cache = None

    def clean(self):
        email = self.cleaned_data['email']
        try:
            user = USER_MODEL._default_manager.get(email__iexact=email)
        except:
            user = None
        self.user_cache = user

        if self.user_cache is None:
            self.add_error('email', "Account does not exist")
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
