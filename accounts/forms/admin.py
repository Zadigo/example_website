from accounts.models import MyUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import ModelForm, ValidationError
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import password_validation
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth import authenticate, get_user_model

USER_MODEL = get_user_model()

class CustomAdminAuthenticationForm(AdminAuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        # NOTE: Despite the backend changes, the
        # field is still has the name 'username' 
        # and not, email
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)

            if self.user_cache is None:
                raise self.get_invalid_login_error()
            self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


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

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)
                
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
