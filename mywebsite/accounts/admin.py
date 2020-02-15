from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.forms import UserChangeForm, UserCreationForm
from accounts.models import MyUser, MyUserProfile, SubscribedUser, MyAnonymousUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'surname', 'is_active',)
    list_filter  = ('is_active',)
    readonly_fields = ('password',)
    search_fields = ['name', 'surname', 'email']

class MyUserProfileAdmin(admin.ModelAdmin):
    actions      = ('activate_account', 'deactivate_account',)
    list_display = ('myuser', 'telephone',)
    search_fields = ['myuser__name', 'myuser__surname', 'myuser__email']

    def activate_account(self, request, queryset):
        queryset.update(actif=True)

    def deactivate_account(self, request, queryset):
        queryset.update(actif=False)

class SubscribedUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_on']
    date_hierarchy = 'created_on'
    list_filter = ['created_on']

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(MyAnonymousUser)
admin.site.register(MyUserProfile, MyUserProfileAdmin)
admin.site.register(SubscribedUser, SubscribedUserAdmin)
admin.site.unregister(Group)
