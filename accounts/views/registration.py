from accounts import forms
from accounts.forms.passwords import (CustomPasswordResetForm,
                                      CustomSetPasswordForm)
from accounts.forms.registration import UserLoginForm, UserSignupForm
from django.contrib import auth, messages
from django.http.response import Http404
from django.shortcuts import redirect, render, reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView, View

USER_MODEL = auth.get_user_model()

class SignupView(FormView):
    form_class = UserSignupForm
    template_name = 'pages/registration/signup.html'
    success_url = '/login'

    @method_decorator(never_cache)
    def post(self, request, *args, **kwargs):
        template_response = super().post(request, *args, **kwargs)
        form = self.form_class(request.POST)
        message = {
            'level': messages.ERROR,
            'extra_tags': 'alert-danger'
        }
        if form.is_valid():
            email = form.cleaned_data['email']
            user = USER_MODEL.objects.filter(email__iexact=email)
            if user.exists():
                message.update({'message': _("Vous possédez déjà un compte chez nous")})
                return redirect('accounts:login')
            else:
                new_user = form.save()
                if new_user:
                    password = form.cleaned_data.get('password2')
                    auth.login(request, auth.authenticate(request, email=email, password=password))
                    return self.get_redirect_url(request)
        else:
           message.update({'message': _("Une erreur est arrivée - SIG-ER")})
        messages.add_message(request, **message)
        return template_response

    def get_redirect_url(self, request, intermediate_view=None, user=None):
        if intermediate_view is None:
            return redirect(request.GET.get('next') or reverse('accounts:profile:home'))

        if user is None:
            return Http404('User could not identified - INT-US')

        request.session['user'] = user.id
        return redirect(intermediate_view)


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
        # the person on the plateform
        form = self.get_form()
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                auth.login(self.request, user)
            return self.form_valid(form)
        else:
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
        auth.logout(request)
        return super().get(request, *args, **kwargs)


class ForgotPasswordView(View):
    """
    A single field form where an unauthenticated user can ask for
    a password reset
    """
    form_class = CustomPasswordResetForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class}
        return render(request, 'pages/registration/forgot_password.html', context)

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            context = {'form': forms.CustomPassowordResetForm}

            user = USER_MODEL.objects.filter(email__iexact=email)
            if user.exists():
                try:
                    # NOTE: Change to append a token to the url
                    # which will help iD the user in the confirm view
                    form.save(request, 'contact.mywebsite@gmail.com')
                except:
                    message = {
                        'message': _("Une erreur est arrivé - EMA-ER"),
                        'level': messages.ERROR,
                        'extra_tags': 'alert-danger'
                    }
                else:
                    message = {
                        'message': _(f"Un email a été envoyé à {email}"),
                        'level': messages.ERROR,
                        'extra_tags': 'alert-success'
                    }
            else:
                message = {
                    'message': _("Nous n'avons pas pu vous trouvez votre addresse mail"),
                    'level': messages.ERROR,
                    'extra_tags': 'alert-danger'
                }

            messages.add_message(request, **message)
            return render(request, 'pages/registration/forgot_password.html', context=context)

        return redirect('accounts:login')


class UnauthenticatedPasswordResetView(View):
    """
    Helps a non authenticated user reset his password
    """
    form_class = CustomSetPasswordForm

    def get(self, request, *args, **kwargs):
        # user_token = request.GET.get('user_token')
        # if not user_token:
        #     return HttpResponseForbidden(reason='Missing argument')
        
        context = {
            'form': self.form_class(USER_MODEL.objects.get(id=1)),
        }
        return render(request, 'pages/registration/forgot_password_confirm.html', context)

    def post(self, request, **kwargs):
        # user_token = request.GET.get('user_token')
        # user = get_object_or_404(USER_MODEL, id=user_token)
        form = self.form_class(user)
        if form.is_valid():
            form.save()
        auth.login(request, user)
        return redirect('profile')
