from django.contrib import admin
from testapp.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
