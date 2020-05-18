from django.db import models
from django.db.models.fields import CharField

class DashboardSetting(models.Model):
    user       = CharField(max_length=56, default='User')
    night_mode = models.BooleanField(default=False)
    other_option = models.BooleanField(default=False)

    def __str__(self):
        return self.user