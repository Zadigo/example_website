from typing import Any, Type, Union

from accounts.forms.profile import AddressProfileForm, BaseProfileForm
from django.forms import Form, ModelForm


PROFILE_FORMS = [
    ('form1', BaseProfileForm),
    ('form2', AddressProfileForm)
]


def get_form_name(name: str, default = None) -> Union[Form, Any]:
    form = list(filter(lambda f: name in f, PROFILE_FORMS))
    if not form:
        if default is not None:
            return default
        raise ValueError(f'{name} does not exist')
    return form[0]


def get_form_by_position(position: int)  -> Union[Form, ModelForm]:
    if position > len(PROFILE_FORMS):
        raise IndexError("Form does not exist")

    for i, values in enumerate(PROFILE_FORMS):
        if i == position:
            break
        
    if not values:
        raise ValueError("Form does not exist")
    return values[1]


def get_initialized_form(position: int, initial: dict = {}):
    form = get_form_by_position(position)
    return form(initial=initial)


def get_form(position: int, request):
    form = get_form_by_position(position)
    return form(request.POST, files=request.FILES)


def get_model_form(position: int, request, instance):
    form = get_form_by_position(position)
    return form(request.POST, files=request.FILES, instance=instance)
