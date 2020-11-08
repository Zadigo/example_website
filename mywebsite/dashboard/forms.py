import datetime
import re
from itertools import filterfalse

from django import forms
from django.contrib.auth import get_user_model
from django.core import exceptions
from django.utils.translation import gettext_lazy as _
from testapp import models

from dashboard import models as dashboard_models
from dashboard import widgets as custom_widgets


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name']


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name']
        widgets = {
            'name': custom_widgets.TextInput(attrs={'plaholder': 'Name'})
        }
