from django.contrib import admin
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib.admin.apps import AdminConfig
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache

from accounts import forms, models

class CustomAdminAuthenticationForm(AdminAuthenticationForm):
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class CustomAdminSite(AdminSite):
    login_form = AdminAuthenticationForm


site = CustomAdminSite()

@admin.register(models.MyUser)
class MyUserAdmin(auth_admin.UserAdmin):
    form = forms.MyUserChangeForm
    add_form = forms.MyUserCreationForm
    model = models.MyUser

    list_display = ['email', 'firstname', 'lastname', 'is_active', 'is_admin']
    list_filter = ()
    filter_horizontal = ()
    ordering = ['email']
    search_fields = ['firstname', 'lastname', 'email']
    fieldsets = [
        ['Details', {'fields': ['firstname', 'lastname']}],
        ['Credentials', {'fields': ['email', 'password']}],
        ['Permissions', {'fields': ['is_admin', 'is_staff', 'is_active']}]
    ]
    add_fieldsets = [
        [None, {
                'classes': ['wide'],
                'fields': ['email', 'password1', 'password2', 'is_admin', 'is_staff', 'is_active']
            }
        ],
    ]
    ordering = ['email']


@admin.register(models.MyUserProfile)
class MyUserProfileAdmin(admin.ModelAdmin):
    actions      = ('activate_account', 'deactivate_account',)
    list_display = ('myuser', 'telephone',)
    search_fields = ['myuser__firstname', 'myuser__lastname', 'myuser__email']

    def activate_account(self, request, queryset):
        queryset.update(actif=True)

    def deactivate_account(self, request, queryset):
        queryset.update(actif=False)

admin.site.unregister(Group)
