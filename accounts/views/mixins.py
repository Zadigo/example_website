from django.contrib import messages
from django.http.response import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail.message import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


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


class IntermedidateViewMixin:
    """
    This mixins adds functionnalities for redirecting to
    and intermediate view just after signup (for example
    to force the user to update certain items in his profile)
    """
    intermediate_pages = []

    def get_redirect_url(self, request, intermediate_view=None, user=None):
        if intermediate_view is None:
            return redirect(request.GET.get('next') or self.success_url)

        if user is None:
            return Http404('User could not identified - INT-US')

        request.session['user'] = user.id
        return redirect(intermediate_view)



class EmailingMixin:
    """
    Adds emailing functionnalities for views that
    require sending emails with a uid token
    """
    email_template_name = None
    subject_template_name = None
    html_email_template_name = None
    token_generator = default_token_generator
    from_email = None
    extra_email_context = {}
    use_https = False

    def send_email(self, request, user):
        current_site = get_current_site(request)
        site_name = current_site.name
        domain = current_site.domain
        # email_field_name = USER_MODEL.get_email_field_name()

        context = {
            'email': user.email,
            'domain': domain,
            'site_name': site_name,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': self.token_generator.make_token(user),
            'protocol': 'https' if self.use_https else 'http',
            **self.extra_email_context
        }

        subject = loader.render_to_string(self.subject_template_name, context)
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(self.email_template_name, context)
        email_message = EmailMultiAlternatives(subject, body, self.from_email, [user.email])

        if self.html_email_template_name is not None:
            html_email = loader.render_to_string(self.html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')
    
        email_message.send()
