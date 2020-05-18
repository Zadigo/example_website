from django.contrib import admin
from dashboard.models import DashboardSetting

@admin.register(DashboardSetting)
class DashboardSettingsAdmin(admin.ModelAdmin):
    list_display = ['user', 'night_mode', 'other_option']
