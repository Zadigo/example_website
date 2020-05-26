from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (DetailView, ListView, TemplateView,
                                  UpdateView, View)

from dashboard import forms
from shop import models, serializers, utilities
from shop.models import Product, ProductOrder
from django.db.models.expressions import Q
from django.contrib.auth import get_user_model

MYUSER = get_user_model()


class IndexView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        products = models.Product.objects.all()
        orders = models.ProductOrder.objects.all()
        context = {
            'products': products,
            'orders': orders,
            'products_count': products.count(),
            'line_chart': [products, orders]
        }
        return render(request, 'index.html', context)

class ProductsView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    queryset = models.Product.objects.all()
    template_name = 'pages/list.html'
    context_object_name = 'products'
    paginate_by = 10

class UsersView(LoginRequiredMixin, generic.ListView):
    model = MYUSER
    queryset = MYUSER.objects.all()
    template_name = 'pages/users.html'
    context_object_name = 'users'
    paginate_by = 10

class SearchView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'pages/search/products.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        searched_item = self.request.GET.get('s')

        # try:
        #     category, search = searched_item.split(':', 1)
        # except:
        #     category = None
        #     search = searched_item
        # else:
        #     if category == "orders":
        #         self.model = models.ProductOrder
        #         self.template_name = 'pages/search/orders.html'
        #     elif category == 'product':
        #         items = queryset.filter(Q(name__icontains=search) | Q(reference__icontains=search))
        #     elif category is None:
        items = queryset.filter(Q(name__icontains=searched_item) 
            | Q(reference__icontains=searched_item) 
            | Q(collection__collection_name__icontains=searched_item)
        )

        return items

class ProductView(LoginRequiredMixin, DetailView):
    """The details of a specific product
    """
    model = models.Product
    queryset = Product.objects.all()
    template_name = 'pages/details.html'
    context_object_name = 'product'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     product = super().get_object()
    #     images = product.images.all()
    #     main_image = images.get(main_image=True)
    #     context['main_image'] = main_image
    #     context['images'] = images
    #     return context

    def get_context_data(self, **kwargs):
        product = super().get_object()
        # We have to pass the user profile here
        # in order to get extra details on the user
        context = super().get_context_data()
        # user_order = super().get_object()
        # userprofile = user_order.user.myuserprofile_set.all()
        # context.update({'userprofile': userprofile})

        # Pass all images that can  be selected
        # for the given product
        # images = models.ProductImage.objects.all()
        # context['available_images'] = images
        return context

class SingleProductOrdersView(LoginRequiredMixin, ListView):
    """Orders for one single product
    """
    model   = models.ProductOrder
    context_object_name = 'orders'
    template_name = 'pages/orders.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = get_object_or_404(models.Product, id=self.kwargs['pk'])
        queryset = queryset.filter(reference=product.reference)
        return queryset

class ProductOrdersView(LoginRequiredMixin, ListView):
    """All the orders made by customers for a specific company
    """
    model   = models.ProductOrder
    queryset = models.ProductOrder.objects.all()
    context_object_name = 'orders'
    template_name = 'pages/orders.html'

    def get_context_data(self):
        context = super().get_context_data()
        return context

    # def get_queryset(self):
    #     # We have to rework the queryset
    #     # in order to return only the orders
    #     # for a specific company
    #     queryset = super().get_queryset()
    #     new_queryset = queryset.filter(seller=self.request.user.id)
    #     return new_queryset

class CreateProductView(LoginRequiredMixin, generic.View):
    max_number_of_steps = 3

    def get(self, request, *args, **kwargs):
        create_form_logic = forms.CreateFormLogic(request)
        return render(request, 'pages/create.html', create_form_logic.context)

    def post(self, request, **kwargs):
        create_form_logic = forms.CreateFormLogic(request)
        create_form_logic.instances = [['collection', 'collection_name', models.ProductCollection]]
        url = create_form_logic.validate_form_and_update_model(models.Product, viewname='dashboard_create')
        return redirect(url)

class UpdateProductView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/update.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, id=kwargs['pk'])
        context.update({'product': {'name': product.name}})
        return context

class CartsView(LoginRequiredMixin, generic.ListView):
    model = models.AnonymousCart
    queryset = models.AnonymousCart.objects.all()
    template_name = 'pages/carts.html'
    context_object_name = 'products'

class ImagesView(LoginRequiredMixin, generic.ListView):
    model = models.ProductImage
    queryset = models.ProductImage.objects.all()
    template_name = 'pages/images.html'
    context_object_name = 'images'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        queryset = super().get_queryset()
        context = super().get_context_data(**kwargs)

        # Pagination for VueJS
        paginator = Paginator(queryset, 8)
        page = self.request.GET.get('page')
        images = paginator.get_page(page)
        images = serializers.ImagesSerializer(instance=images.object_list, many=True)
        context['vue_images'] = images.data
        return context

@login_required
def deleteview(request, **kwargs):
    method = kwargs['method']
    if method == 'products':
        item = get_object_or_404(models.Product, id=kwargs['pk'])

    if method == 'carts':
        item = get_object_or_404(models.AnonymousCart, id=kwargs['pk'])

    item.delete()
    url = f'dashboard_{method}'
    return redirect(reverse(url))

class Settings(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        return render(request, 'settings.htm', {})
