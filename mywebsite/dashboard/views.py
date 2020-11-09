import json

from django.core.cache import cache
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from requests import get as get_request


class IndexView(TemplateView):
    template_name = 'pages/index.html'
    

class ProductsView(TemplateView):
    template_name = 'pages/products.html'

    def post(self, request, **kwargs):
        items = cache.get('items')
        if items is None:
            response = get_request('https://jsonplaceholder.typicode.com/todos')
            items = response.json()
            cache.set('items', items, timeout=300)
        return JsonResponse(data=json.dumps(items), safe=False)


class ProductView(TemplateView):
    template_name = 'pages/edit/product.html'


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
