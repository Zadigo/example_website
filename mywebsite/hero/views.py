from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from django.core.mail import send_mail


# @method_decorator(cache_page(240 * 60), name='dispatch')
class HeroView(TemplateView):
    template_name = 'pages/home.html'


@require_POST
def send_message(request, **kwargs):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    send_mail(
        '',
        message=message,
        from_email='',
        recipient_list=[email]
    )
    return JsonResponse(data={})
