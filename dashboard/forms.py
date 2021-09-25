from django.forms import Form, ModelForm, fields
from django.forms.fields import CharField

from dashboard.models import DashboardSetting


class TestForm(Form):
    name = CharField(max_length=50)

class DashboardSettingForm(ModelForm):
    class Meta:
        model = DashboardSetting
        fields = ['dark_mode']
        widgets = {
            'dark_mode': None
        }

