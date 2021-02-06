from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.forms.fields import CharField, EmailField
from django.forms.widgets import EmailInput, PasswordInput
from django.utils.translation import gettext_lazy as _


class CustomPasswordResetForm(PasswordResetForm):
    email = EmailField(
        label=_('Email'),
        max_length=254,
        widget=EmailInput(
            attrs={'class': 'form-control', 'autocomplete': 'email', 'placeholder': 'Email'}
        )
    )

    def save(self, request, from_email):
        super().save(
            from_email=from_email,
            subject_template_name='components/emails/password_reset_subject.txt',
            email_template_name='components/emails/password_reset_email.html',
            request=request
        )


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = CharField(
        label=_('Nouveau mot de passe'),
        widget=PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Nouveau mot de passe','autocomplete': 'off'}
        ),
        strip=False
    )
    new_password2 = CharField(
        label=_('Nouveau mot de passe confirmation'),
        widget=PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Nouveau mot de passe confirmation', 'autocomplete': 'off'}
        ),
        strip=False,
    )


class CustomChangePasswordForm(CustomSetPasswordForm):
    old_password = CharField(
        label=_("Old password"),
        strip=False,
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ancien mot de passe',
                                          'autocomplete': 'current-password', 'autofocus': True}),
    )
