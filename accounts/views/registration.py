from accounts.forms.passwords import (CustomPasswordResetForm,
                                      CustomSetPasswordForm)
from accounts.forms.registration import SendActivationEmailForm, UserLoginForm, UserSignupForm
from accounts.views.mixins import (EmailingMixin, IntermedidateViewMixin,
                                   MessagesMixin)
from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetConfirmView
from django.core.exceptions import ValidationError
from django.http.response import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from django.views.generic.base import View

USER_MODEL = get_user_model()

class SignupView(IntermedidateViewMixin, EmailingMixin, FormView):
    """
    Allows a user to create an account
    """
    form_class = UserSignupForm
    template_name = 'pages/registration/signup.html'
    success_url = reverse_lazy('accounts:login')

    email_template_name = 'includes/emails/account_activation_email.html'
    subject_template_name = 'includes/emails/account_activation_email.txt'
    html_email_template_name = None
    
    @method_decorator(sensitive_post_parameters('password1', 'password2'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def post(self, request, *args, **kwargs):
        template_response = super().post(request, *args, **kwargs)
        message = {'level': messages.ERROR, 'extra_tags': 'alert-danger'}

        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']

            user = authenticate(request, email=email, password=password)
            if user is not None:
                message.update({'message': _('Vous possédez déjà un compte')})
                return redirect(self.success_url)

            # else:
            #     user = form.save()
            #     login(request, user, backend='accounts.backends.EmailAuthenticationBackend')
            # return self.get_redirect_url(request) 

            # Send an email to the address in order
            # to confirm the it
            cleaned_data = {}
            for key, value in form.cleaned_data.items():
                if key != 'password1' and key != 'password2':
                    cleaned_data[key] = value
                
                if key == 'password2':
                    cleaned_data['password'] = value

            user = USER_MODEL.objects.create_user(**cleaned_data)
            # NOTE: Optionnally send an activation email to user
            # when a new account is created. This flow can be
            # controlled by a setting in the database 
            # ACTIVATION_EMAIL_ON_SIGNUP
            self.from_email = getattr(settings, 'EMAIL_HOST_USER')
            activation_email_on_signup = getattr(settings, 'ACTIVATION_EMAIL_ON_SIGNUP', False)
            if activation_email_on_signup:
                try:
                    self.send_email(request, user)
                except:
                    raise forms.ValidationError('Could not send activation email')
            else:
                # If an activation email is not
                # required, set the user as active
                user.is_active = True
                user.save()
            return self.get_redirect_url(request)   
        else:
           message.update({'message': _('Une erreur est arrivée - SIG-ER')})
        messages.add_message(request, **message)
        return template_response


class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'pages/registration/login.html'
    success_url = '/'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def post(self, request, *args, **kwargs):
        # The authentication happens in the form
        # itself. If a user was returned via the
        # user_cache, then use that obj to login
        # that person
        form = self.get_form()
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(self.request, user)
                return self.form_valid(form)
        return self.form_invalid(form)

    def get_form_kwargs(self):
        # Updated in order to instantiate
        # the form with the request object
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class LogoutView(RedirectView):
    url = '/'
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class ForgotPasswordView(MessagesMixin, FormView):
    """
    Allows the user to request a new password
    """
    form_class = CustomPasswordResetForm
    template_name = 'pages/registration/forgot_password.html'
    success_url = '/accounts/login'

    def post(self, request, *args, **kwargs):
        form = super().get_form()
        if form.is_valid():
            form.save(request, getattr(settings, 'EMAIL_HOST_USER'))
        else:
            return super().form_invalid(form)
        return super().form_valid(form)


class PasswordResetView(PasswordResetConfirmView):
    """
    Helps a non authenticated user reset their password
    """
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'pages/registration/forgot_password_confirm.html'


class SendActivationEmailView(EmailingMixin, FormView):
    """
    Allows a user to send an account activation
    link to his email account
    """
    form_class = SendActivationEmailForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'pages/registration/send_activation.html'
    
    email_template_name = 'includes/emails/account_activation_email.html'
    subject_template_name = 'includes/emails/account_activation_email.txt'
    html_email_template_name = None

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.get_user()
            if not user.is_active:
                self.send_email(request, user)
            return redirect(reverse('accounts:login'))
        return self.form_invalid(form)


class AccountActivationView(View):
    """
    Allows a user to activate his account
    """
    def get(self, request, *args, **kwargs):
        if 'uidb64' not in kwargs and 'token' not in kwargs:
            return HttpResponseForbidden('Forbidden - MT-UID')
        
        try:
            uid = urlsafe_base64_decode(kwargs['uidb64']).decode()
            user = USER_MODEL._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, USER_MODEL.DoesNotExist, ValidationError):
            user = None

        # result = default_token_generator.check_token(user, kwargs['token'])
        # if not result:
        #     return HttpResponseForbidden('Forbidden - CHK-RES')

        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.save()
            # user.sendmail()

        return render(request, 'pages/registration/activation.html', {})
