from django.template import Library
from django.template.context import Context
from django.template.loader import get_template


register = Library() 

@register.filter
def inputfield(field, template_pack=None):
    c = field.field.widget.get_context(field.name, field.value, {'class': 'form-control'})
    t = get_template('widgets/input.html')
    return t.render(c)

from django.forms.boundfield import BoundField
from django.forms.widgets import TextInput
