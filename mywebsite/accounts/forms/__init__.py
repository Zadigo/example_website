from django.forms import ModelForm
from accounts.forms.profile import BaseProfileForm, AddressProfileForm


PROFILE_FORMS = [
    ('form1', BaseProfileForm),
    ('form2', AddressProfileForm)
]



def get_profile_form_by_name(name, initital: dict = {}) -> ModelForm:
    form = list(filter(lambda n: n in PROFILE_FORMS))
    if not form:
        raise ValueError(f'{name} does not exist')
    if not initital:
        return form[0]
    return form[0](initital=initital)


def get_form_by_position(position):
    for i, values in enumerate(PROFILE_FORMS):
        if i == position:
            break
        if position > i:
            raise IndexError("Form does not exist")
    if not values:
        raise ValueError("Form does not exist")
    return values[0]
