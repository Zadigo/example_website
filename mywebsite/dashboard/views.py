from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, View
from django.db.models import F

from dashboard.forms import CreateProductForm, CreateProductFormII, FormSelector
from django.shortcuts import reverse, redirect
from dashboard import models


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/index.html')

class CreateNewView(View):
    selector = FormSelector(max_steps=2)

    def get(self, request, *args, **kwargs):
        self.selector.request = request
        return render(request, 'pages/create.html', self.selector.get_context())

    def post(self, request, *args, **kwargs):
        self.selector.request = request
        self.selector.post(request, instance=None)
        return redirect(self.selector.url)

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

    def post(self, request, **kwargs):
        user_settings = models.DashboardSetting.objects.get(id__exact=1)
        if user_settings.exists():
            if 'nightmode' in kwargs:
                current_state_is_true = user_settings.nightmode
                if current_state_is_true:
                    user_settings.night_mode = False
                else:
                    user_settings.night_mode = True
                user_settings.save()
        return JsonResponse(data={'status': 'Saved'})

class DashboardLoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/login.html')

# MISC

class ListItemsCardsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/list_cards.html')

class UserDetailsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/profile.html')