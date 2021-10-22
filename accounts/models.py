import os
from datetime import datetime

import stripe
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, Group, Permission,
                                        PermissionsMixin,
                                        _user_get_permissions,
                                        _user_has_module_perms, _user_has_perm)
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from accounts.managers import MyUserManager
from accounts.utils import avatar_dir


class PermissionsMixin(models.Model):
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False, 
        help_text=_(
            'Gives all permissions '
            'to a designated user'
        )
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='user_set',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='user_set',
        related_query_name='user'
    )

    class Meta:
        abstract = True

    def get_user_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'user')

    def get_group_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'group')

    def get_all_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'all')

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        if self.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)


class MyUser(AbstractBaseUser, PermissionsMixin):
    """Base user model for those user accounts"""
    email       = models.EmailField(max_length=255, unique=True)
    firstname      = models.CharField(max_length=100, null=True, blank=True)
    lastname         = models.CharField(max_length=100, null=True, blank=True)
    
    is_active        = models.BooleanField(default=True)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    # def has_perm(self, perm, obj=None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True
    
    # @property
    # def is_superuser(self):
    #     return all([self.is_staff, self.is_admin, self.is_active])

    @property
    def get_full_name(self):
        return f'{self.firstname} {self.lastname}' 

    @property
    def get_short_name(self):
        return self.firstname

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class MyUserProfile(models.Model):
    """User profile model used to complete the base user model"""

    myuser = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=avatar_dir, blank=True, null=True)
    avatar_thumbnail = ImageSpecField(
        processors=[ResizeToFill(width=100, height=100)],
        format='JPEG', 
        options={'quality': 70}
    )

    customer_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=True,
        help_text='Stripe customer ID'
    )
    birthdate = models.DateField(default=timezone.now, blank=True, null=True)
    telephone   = models.CharField(max_length=20, blank=True, null=True)
    address    = models.CharField(max_length=150, blank=True, null=True)
    city        = models.CharField(max_length=100, blank=True, null=True)
    zip_code    = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.myuser.email

    @property
    def get_full_address(self):
        return f'{self.address}, {self.city}, {self.zip_code}'

    @property
    def is_birthday(self):
        return self.birthdate == datetime.now().date()

    def clean(self, *args, **kwargs):
        try:
            details = stripe.Customer.create(
                email=self.myuser.email, 
                name=self.myuser.get_full_name
            )
        except stripe.error.StripeError as e:
            # Silently fail if we cannot create
            # a Stripe customer
            pass
        else:
            self.customer_id = details['customer_id']


@receiver(post_save, sender=MyUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyUserProfile.objects.create(myuser=instance)


@receiver(post_delete, sender=MyUserProfile)
def delete_old_avatar(sender, instance, **kwargs):
    is_s3_backend = False
    try:
        is_s3_backend = settings.USE_S3
    except:
        pass

    if not is_s3_backend:
        # if instance.avatar.url is not None:
        if getattr(instance.avatar, '_file') is not None:
            if os.path.isfile(instance.avatar.path):
                os.remove(os.avatar.path)
    else:
        instance.url.delete(save=False)


@receiver(pre_save, sender=MyUserProfile)
def delete_avatar_on_update(sender, instance, **kwargs):
    is_s3_backend = False
    try:
        is_s3_backend = settings.USE_S3
    except:
        pass

    if not is_s3_backend:
        if instance.pk:
            try:
                current_profile = MyUserProfile.objects.get(id=instance.pk)
                old_image = current_profile.avatar
            except:
                return False
            else:
                new_image = instance.avatar
                if old_image and old_image != new_image:
                    if os.path.isfile(old_image.path):
                        os.remove(old_image.path)
    else:
        instance.url.delete(save=False)
