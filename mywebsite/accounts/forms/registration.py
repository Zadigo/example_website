from accounts.forms.base import AuthenticationForm
from accounts.models import MyUser
from accounts.widgets import EmailInput, PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, ValidationError, fields, widgets
from django.utils.crypto import get_random_string, salted_hmac
from django.utils.translation import gettext_lazy as _


class UserLoginForm(AuthenticationForm):
    # token = fields.CharField(max_length=50, min_length=50, widget=TextInput())
    pass


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

        return self.cleaned_data
