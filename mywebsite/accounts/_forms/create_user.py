from accounts import widgets as custom_widgets
from accounts.models import MyUser, MyUserProfile
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import password_validation
from django.contrib.auth.tokens import default_token_generator
from django.forms import fields, widgets
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _


class UserCreationForm(forms.ModelForm):
    password1 = fields.CharField(label=_('Password'), widget=widgets.PasswordInput)
    password2 = fields.CharField(label=_('Password confirmation'), widget=widgets.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email', 'is_admin', 'is_staff']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user
