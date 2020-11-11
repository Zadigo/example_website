import json

from django.contrib.messages import success
from django.core.cache import cache
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from requests import get as get_request


class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.TestForm

        charts = {
            'barchart': {
                'labels': ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                'data': [12, 19, 3, 5, 2, 3]
            }
        }
        context['charts'] = charts
        return context
    

class ProductsView(TemplateView):
    template_name = 'pages/products.html'

    def post(self, request, **kwargs):
        items = cache.get('items')
        if items is None:
            response = get_request('https://jsonplaceholder.typicode.com/todos')
            items = response.json()
            cache.set('items', items, timeout=300)
        return JsonResponse(data=json.dumps(items), safe=False)


@method_decorator(cache_page(15 * 60), name='dispatch')
class ProductView(TemplateView):
    template_name = 'pages/edit/product.html'

    def post(self, request, **kwargs):
        success(request, 'Item was updated', extra_tags='alert-success')
        return redirect('dashboard:product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_mode'] = True
        return context


@method_decorator(cache_page(15 * 60), name='dispatch')
class SettingsHomeView(TemplateView):
    template_name = 'pages/settings/home.html'


@method_decorator(cache_page(15 * 60), name='dispatch')
class SettingsGeneralView(TemplateView):
    template_name = 'pages/settings/general.html'


@require_POST
def duplicate_products(request, **kwargs):
    return JsonResponse(data={})


@require_POST
def delete_products(request, **kwargs):
    return JsonResponse(data={})


@require_POST
def download_csv(request, **kwargs):
    selected_items = request.POST.get('selecteditems', None)
    if selected_items is None:
        pass
    else:
        pass
    return JsonResponse(data={})
