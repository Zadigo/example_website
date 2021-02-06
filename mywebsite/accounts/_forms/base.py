from django.forms import Form
from django.forms.fields import CharField


class BaseFormMixin(Form):
    token = CharField(max_length=100, required=True)

    def __init__(self, data, **kwargs):
        super().__init__(data=data, **kwargs)
