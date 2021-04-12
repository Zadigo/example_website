from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

MYUSER = get_user_model()

class DashboardSetting(models.Model):
    user = models.ForeignKey(MYUSER, on_delete=models.CASCADE)
    dark_mode = models.BooleanField(default=False)

    def __str__(self):
        return self.user

    def save(self, **kwargs):
        created = self.pk is None
        super().save(**kwargs)
        if created:
            self.objects.create(user=None)


# @receiver(post_save, sender=MYUSER)
# def create_user_settings(sender, instance, created, **kwargs):
#     if created:
#         DashboardSetting.objects.create(user=instance)
