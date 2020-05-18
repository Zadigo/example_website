from django.db import models
from dashboard import managers

class DashboardSetting(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    likes = models.PositiveIntegerField()

    objects = models.Manager()
    dashboard_manager = managers.DashboardManager.as_manager()

    def __str__(self):
        return self.name