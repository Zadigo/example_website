from django.contrib import messages
from django.http.response import Http404
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail.message import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


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
