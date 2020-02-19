from django.shortcuts import render
from django.views.generic import View, CreateView
from django.http.response import JsonResponse
from django.conf import settings

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/index.html')

class CreateNewView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/create.html')

class UpdateItemView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/update.html')

class ItemDetailsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/details.html')

class ListItemsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/list.html')

    def post(self, request, **kwargs):
        import os
        import json
        path = os.path.join(settings.MEDIA_URL, 'products.json')
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse(data['products'], status=200)

class SettingsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/settings.html')

class DashboardLoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/login.html')