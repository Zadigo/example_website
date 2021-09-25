from accounts.models import MyUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import ModelForm, ValidationError
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput
from django.utils.translation import gettext_lazy as _


class MyUserChangeForm(ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            'Raw passwords are not stored, so there is no way to see this '
            'user’s password, but you can change the password using '
            '<a href="{}">this form</a>.'
        )
    )

    class Meta:
        model = MyUser
        fields = '__all__'


class MyUserCreationForm(ModelForm):
    password1 = CharField(label=_('Password'), widget=PasswordInput())
    password2 = CharField(label=_('Password confirmation'), widget=PasswordInput())

    class Meta:
        model = MyUser
        fields = ['email', 'is_admin', 'is_staff']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Passwords do not match"))

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user
