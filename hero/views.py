from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model


class HeroView(TemplateView):
    template_name = 'pages/home.html'
    # template_name = '_new/home.html'


@require_POST
def send_message(request, **kwargs):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    # user = None

    # USER_MODEL = get_user_model()
    # queryset = USER_MODEL.objects.filter(email__exact=email)
    # if queryset.exists():
    #     user = queryset.get()

    send_mail(
        '',
        message=message,
        from_email='',
        recipient_list=[email]
    )
    return JsonResponse(data={})
