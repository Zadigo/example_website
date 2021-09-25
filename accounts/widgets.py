from django.forms import widgets
from django.utils.translation import gettext_lazy as _


class CustomInput(widgets.Input):
    input_type = 'text'

    def get_context(self, name, value, attrs):
        if attrs is None:
            attrs = dict()
        attrs['class'] = 'form-control'
        context = super().get_context(name, value, attrs)
        return context


class PasswordInput(CustomInput):
    input_type = 'password'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['placeholder'] = _('Password')
        return context


class TextInput(CustomInput):
    template_name = 'widgets/input.html'


class EmailInput(CustomInput):
    input_type = 'email'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['autocomplete'] = 'email'
        context['widget']['attrs']['placeholder'] = _('Email')
        return context


class TelephoneInput(TextInput):
    input_type = 'tel'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['autocomplete'] = 'tel'
        return context


class FirstNameInput(TextInput):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['autocomplete'] = 'given-name'
        return context


class LastNameInput(TextInput):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['autocomplete'] = 'family-name'
        return context


class AddressLineOne(TextInput):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['autocomplete'] = 'street-address'
        return context
