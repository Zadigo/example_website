from django.views.generic import TemplateView
from django.http import JsonResponse

class HeroView(TemplateView):
    template_name = 'home/hero.html'

    def post(self, request, **kwargs):
        return JsonResponse({'success': 'success'})