import csv
import io
import json
import random
import re

from django import http
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import exceptions
from django.core.mail import send_mail, send_mass_mail
from django.core.paginator import Paginator
from django.db import transaction as atomic_transactions
from django.db.models.expressions import F, Q
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.decorators import method_decorator
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import (require_GET, require_http_methods,
                                          require_POST)
from testapp import models

from dashboard import forms

# from dashboard import models as dashboard_models
# from shop import choices, models, serializers, utilities


MYUSER = get_user_model()


class IndexView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'pages/home.html', context)


class ProductsView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'pages/lists/products.html'
    context_object_name = 'products'
    paginate_by = 10

    # def get(self, request, *args, **kwargs):
    #     get_request = super().get(request, *args, **kwargs)
    #     # This section resets the next_for_update in the
    #     # session to prevent persistence when trying to
    #     # return to the product page
    #     previous_searched_terms = self.request.session.get('next_for_update')
    #     if previous_searched_terms:
    #         self.request.session.pop('next_for_update')
    #     return get_request

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     paginator = Paginator(self.queryset, self.paginate_by)
    #     page = self.request.GET.get('page')
    #     products = paginator.get_page(page)
        
    #     serialized_products = serializers.SimpleProductSerializer(
    #                                 instance=products.object_list, many=True)
    #     context['on_current_page'] = serialized_products.data
    #     context['number_of_items'] = self.queryset.count()
    #     return context


class SearchView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'pages/lists/search/products.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['search'] = searched_term = self.request.GET.get('s')
        self.request.session.update({'next_for_update': searched_term})
        return context

    def get_queryset(self):
        searched_terms = self.request.GET.get('s')
        return []


class CreateProductView(LoginRequiredMixin, generic.CreateView):
    model = models.Product
    queryset = models.Product.objects.all()
    form_class = forms.CreateProductForm
    template_name = 'pages/edit/create/product.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('dashboard:products:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_to_view'] = reverse('dashboard:products:create')

        # This triggers the apparation or
        # not of certain features on the update
        # and creation page. For instance, unlinking
        # an image on the creation is not necessary
        context['vue_edit_mode'] = 'create'
        return context


class UpdateProductView(LoginRequiredMixin, generic.UpdateView):
    model = models.Product
    template_name = 'pages/edit/update/product.html'
    form_class = forms.UpdateProductForm
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = super().get_object()
        # context['post_to_view'] = reverse('dashboard:products:update', args=[product.id])

        # If we clicked update from the search page,
        # this method allows to return that same
        # search page as opposed to all the products
        context['return_to_search'] = self.request.session.get('next_for_update') or None

        # This section allows the user
        # to navigate from product to
        # product in the updae page
        # <- and -> arrows
        # queryset = super().get_queryset()
        # queryset_list = list(queryset.values_list('id', flat=True))
        # queryset_list_length = len(queryset_list)
        # current_product_index = queryset_list.index(product.id)

        # next_product_index = current_product_index + 1
        # if next_product_index == queryset_list_length:
        #     next_product_index = 0
        #     context['disable_next'] = True

        # context['previous_product'] = reverse('dashboard:products:update', args=[queryset_list[current_product_index - 1]])
        # context['next_product'] = reverse('dashboard:products:update', args=[queryset_list[next_product_index]])

        # serialized_product = serializers.ProductSerializer(instance=product)
        # context['vue_product'] = serialized_product.data

        # images = models.Image.objects.all()
        # context['images'] = images = images.exclude(id__in=product.images.values_list('id'))
        # serialized_other_images = serializers.ImageSerializer(images, many=True)
        # context['vue_other_images'] = serialized_other_images.data

        # This triggers the apparation or
        # not of certain features on the update
        # and creation page. For instance, unlinking
        # an image on the creation is not necessary
        context['vue_edit_mode'] = 'update'
        return context

    def get_success_url(self):
        product = super().get_object()
        return reverse('dashboard:products:update', args=[product.id])


# @method_decorator(atomic_transactions.atomic, name='post')
# class ImageView(LoginRequiredMixin, generic.UpdateView):
#     model = models.Image
#     queryset = models.Image.objects.all()
#     form_class = forms.ImageForm
#     template_name = 'pages/edit/update/image.html'
#     context_object_name = 'image'

#     def get_success_url(self):
#         image = super().get_object()
#         return reverse('dashboard:images:update', args=[image.id])


# class SettingsView(LoginRequiredMixin, generic.TemplateView):
#     template_name = 'pages/edit/update/settings/index.html'
    
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     user = self.request.user
#     #     try:
#     #         user_store = dashboard_models.DashboardSetting.objects.get(user=self.request.user)
#     #     except:
#     #         user_has_store = False
#     #     else:
#     #         user_has_store = True
#     #         context['store'] = user_store
#     #     context['user_has_store'] = user_has_store
#     #     return context


# class DashboardSettingsMixin:
#     def custom_post(self, request, redirect_url, form, **kwargs):
#         form = form(request.POST)
#         if form.errors:
#             messages.error(request, f'Le formulaire possède des erreurs: {[error for error in form.errors.keys()]}', extra_tags='alert-danger')
#         if form.is_valid():
#             item = dashboard_models.DashboardSetting.objects.filter(id=request.user.id)
#             item.update(**form.cleaned_data)
#         return redirect(reverse(redirect_url))


# class GeneralSettingsView(LoginRequiredMixin, generic.View):
#     def get(self, request, *args, **kwargs):
#         user = request.user
#         setting = dashboard_models.DashboardSetting.objects.get(myuser=user)
#         context = {
#             'store': dashboard_models.DashboardSetting.objects.get(myuser=user),
#             'form': forms.DashboardSettingsForm(
#                 initial={
#                     'name': setting.name,
#                     'legal_name': setting.legal_name,
#                     'telephone': setting.telephone,
#                     'contact_email': setting.contact_email,
#                     'customer_care_email': setting.customer_care_email,
#                     'automatic_archives': setting.automatic_archive
#                 }
#             )
#         }
#         return render(request, 'pages/edit/update/settings/general.html', context)

#     def post(self, request, **kwargs):
#         form = forms.DashboardSettingsForm(request.POST)
#         if form.errors:
#             messages.error(request, f'Le formulaire possède des erreurs: {[error for error in form.errors.keys()]}', extra_tags='alert-danger')
#         if form.is_valid():
#             item = dashboard_models.DashboardSetting.objects.filter(id=request.user.id)
#             item.update(**form.cleaned_data)
#         return redirect(reverse('dashboard:settings:general'))


# class StoreSettingsView(LoginRequiredMixin, generic.UpdateView):
#     model = dashboard_models.DashboardSetting
#     form_class = forms.DashboardSettingsForm
#     success_url = '/dashboard/settings'
#     context_object_name = 'store'
#     template_name = 'pages/edit/update/settings/shop.html'


# class AnalyticsSettingsView(LoginRequiredMixin, DashboardSettingsMixin, generic.View):
#     def get(self, request, *args, **kwargs):
#         user = request.user
#         setting = dashboard_models.DashboardSetting.objects.get(myuser=user)
#         context = {
#             'store': dashboard_models.DashboardSetting.objects.get(myuser=user),
#             'form': forms.AnalyticsSettingsForm(
#                 initial={
#                     'google_analytics': setting.google_analytics,
#                     'google_tag_manager': setting.google_tag_manager,
#                     'google_optimize': setting.google_optimize,
#                     'google_ads': setting.google_ads,
#                     'facebook_pixels': setting.facebook_pixels,
#                     'mailchimp': setting.mailchimp
#                 }
#             )
#         }
#         return render(request, 'pages/edit/update/settings/analytics.html', context)

#     def post(self, request, **kwargs):
#         return self.custom_post(request, 'dashboard:settings:analytics', forms.AnalyticsSettingsForm, **kwargs)


# class CouponsView(LoginRequiredMixin, generic.ListView):
#     model = models.Discount
#     queryset = models.Discount.objects.all()
#     template_name = 'pages/lists/coupons.html'
#     context_object_name = 'coupons'


# class CreateCouponsView(LoginRequiredMixin, generic.CreateView):
#     model = models.Discount
#     form_class = forms.DiscountForm
#     queryset = models.Discount.objects.all()
#     template_name = 'pages/edit/create/coupon.html'
#     context_object_name = 'coupon'


# class UpdateCouponsView(LoginRequiredMixin, generic.UpdateView):
#     model = models.Discount
#     form_class = forms.DiscountForm
#     queryset = models.Discount.objects.all()
#     template_name = 'pages/edit/update/coupon.html'
#     context_object_name = 'coupon'

#     def get_success_url(self):
#         coupon = super().get_object()
#         return reverse('dashboard:coupons:update', args=[coupon.id])


# class CollectionsView(LoginRequiredMixin, generic.ListView):
#     model = models.ProductCollection
#     queryset = models.ProductCollection.objects.all()
#     template_name = 'pages/lists/collections.html'
#     context_object_name = 'collections'
#     paginate_by = 10


# class CreateCollectionView(LoginRequiredMixin, generic.CreateView):
#     model = models.ProductCollection
#     form_class = forms.CollectionForm
#     template_name = 'pages/edit/create/collection.html'
#     context_object_name = 'collection'
#     success_url = '/dashboard/collections'


# class UpdateCollectionView(LoginRequiredMixin, generic.UpdateView):
#     model = models.ProductCollection
#     form_class = forms.CollectionForm
#     template_name = 'pages/edit/update/collection.html'
#     context_object_name = 'collection'

#     def get_success_url(self):
#         product = super().get_object()
#         return reverse('dashboard:collections:update', args=[product.id])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         second_conditions = [
#             {'id': i, 'name': condition[0]} 
#                 for i, condition in enumerate(choices.SecondConditionsChoices.choices)
#         ]
#         context['vue_second_conditions'] = second_conditions
#         return context


@csrf_exempt
@login_required
@require_POST
def upload_csv(request):
    pass


@csrf_exempt
@login_required
@require_http_methods(['GET', 'POST'])
def download_csv(request):
    pass


@login_required
@atomic_transactions.atomic
@require_POST
def table_actions(request, **kwargs):
    method = request.POST.get('method')
    if not method or method == 'not-selected':
        messages.error(request, "Actions non reconnue - TAB-AC", extra_tags='alert-danger')
        return redirect(request.GET.get('next') or 'dashboard:home')

    authorized_methods = [
        'activate', 'deactivate', 'duplicate', 'delete', 'archive'
    ]
    if method not in authorized_methods:
        messages.error(request, "Actions non reconnue - TAB-AC", extra_tags='alert-danger')
        return redirect(request.GET.get('next') or 'dashboard:home')

    keys = request.POST.getlist('key')
    if not keys:
        messages.error(request, "Aucun éléments n'a été sélectionnés", extra_tags='alert-warning')
        return redirect(request.GET.get('next') or 'dashboard:home')

    products = models.Product.objects.filter(id__in=keys)
    number_of_products = products.count()

    if not products.exists():
        messages.warning(request, "Aucun élément n'a été trouvé", extra_tags='alert-warning')
        return redirect(request.GET.get('next') or 'dashboard:home')
    
    if number_of_products > 1:
        message_text = '{prefix} éléments ont été {suffix}s'
    else:
        message_text = '{prefix} élément a été {suffix}'

    message = {
        'level': messages.SUCCESS,
        'extra_tags': 'alert-success'
    }
    if method == 'activate':
        non_active_products = products.filter(active=False)
        non_active_products.update(active=True)
        message['message'] = message_text.format(prefix=number_of_products, suffix='activé')

    if method == 'deactivate':
        active_products = products.filter(active=True)
        active_products.update(active=False)
        message['message'] = message_text.format(prefix=number_of_products, suffix='désactivé')

    if method == 'duplicate':
        new_items = [
            models.Product(
                name=f'Copie de {product.name}',
                active=False
            ) for product in products
        ]
        models.Product.objects.bulk_create(new_items)
        message['message'] = message_text.format(prefix=number_of_products, suffix='dupliqué')

    if method == 'delete':
        products.delete()
        message['message'] = message_text.format(prefix=number_of_products, suffix='supprimé')

    if method == 'archive':
        message['message'] = message_text.format(prefix=number_of_products, suffix='archivé')

    messages.add_message(request, **message)
    return redirect(request.GET.get('next') or 'dashboard:home')


# @login_required
# @atomic_transactions.atomic
# @views_decorators.require_GET
# def delete_item_via_table(request, **kwargs):
#     """
#     Delete an element from the database via a table
#     """
#     method = kwargs['method']

#     if method == 'products':
#         item = get_object_or_404(models.Product, id=kwargs['pk'])

#     if method == 'carts':
#         item = get_object_or_404(models.Cart, id=kwargs['pk'])
#         # Check if the cart has orders and if so,
#         # mark them as terminated or completed
#         item.customerorder_set.all().update(completed=True)

#     item.delete()

#     url = f'dashboard:{method}:home'

#     if method == 'carts':
#         url = f'dashboard:carts'

#     page = request.GET.get('page')
#     url = reverse(url)
#     if page:
#         url = f'{url}?page={page}'

#     messages.success(request, f"L'élément a été supprimé", extra_tags='alert-success')
#     return redirect(url)


@login_required
@atomic_transactions.atomic
@require_GET
def delete_product(request, **kwargs):
    """
    Delete a product from the update page
    """
    item = get_object_or_404(models.Product, id=kwargs['pk'])
    item.delete()
    messages.success(request, f"{item.name} a été supprimé", extra_tags='alert-success')
    return redirect('dashboard:products:home' or request.GET.get('next'))


@login_required
@require_POST
def duplicate_view(request, **kwargs):
    state = False
    base_message = {
        'request': request
    }
    try:
        product = models.Product.objects.get(id=kwargs['pk'])
    except:
        base_message.update(
            {
                'message': "Le produit n'a pas pu être dupliqué - DUP-NE", 
                'extra_tags': 'alert-danger'
            }
        )
        messages.error(**base_message)
        return http.JsonResponse(data={'state': state}, code=400)

    base = {
        'name': f'Copie de {product.name}',
    }

    try:
        with atomic_transactions.atomic():
            new_product = models.Product.objects.create(**base)
    except:
        base_message.update(
            {
                'message': "Le produit n'a pas pu être dupliqué - DUP-NP",
                'extra_tags': 'alert-warning'
            }
        )
        messages.error(**base_message)
        return http.JsonResponse(data={'state': state}, code=400)
    
    base_message.update({
        'message': f"{new_product.name} a été créer",
        'extra_tags': 'alert-success'
    })
    messages.success(**base_message)
    return http.JsonResponse(data={'redirect_url': reverse('dashboard:products:update', args=[new_product.id])})
