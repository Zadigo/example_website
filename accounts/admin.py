from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from accounts.forms.admin import CustomAdminAuthenticationForm, MyUserChangeForm, MyUserCreationForm
from accounts.models import MyUser, MyUserProfile


class CustomAdminSite(AdminSite):
    login_form = CustomAdminAuthenticationForm
    model = MyUser

site = CustomAdminSite()


class MyUserAdmin(auth_admin.UserAdmin):
    # form = MyUserChangeForm
    add_form = MyUserCreationForm

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


class MyUserProfileAdmin(admin.ModelAdmin):
    list_display = ['myuser', 'telephone']
    actions = ['activate_account', 'deactivate_account']
    search_fields = ['myuser__firstname', 'myuser__lastname', 'myuser__email']

    def activate_account(self, request, queryset):
        queryset.update(actif=True)

    def deactivate_account(self, request, queryset):
        queryset.update(actif=False)


site.register(MyUser, MyUserAdmin)
site.register(MyUserProfile, MyUserProfileAdmin)
