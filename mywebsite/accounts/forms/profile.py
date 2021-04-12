from accounts import widgets
from accounts.models import MyUser, MyUserProfile
from django.forms import ModelForm


class BaseProfileForm(ModelForm):
    class Meta:
        model   = MyUser
        fields  = ['firstname', 'lastname', 'email']
        widgets = {
            'firstname': widgets.FirstNameInput(attrs={'placeholder': 'John'}),
            'lastname': widgets.LastNameInput(attrs={'placeholder': 'Doe'}),
            'email': widgets.TextInput(attrs={'placeholder': 'john.doe@gmail.com'}),
        }


class AddressProfileForm(ModelForm):
    class Meta:
        model   = MyUserProfile
        fields  = ['address', 'city', 'zip_code']
        widgets = {
            'address': widgets.AddressLineOne(attrs={'placeholder': '173 rue de Rivoli'}),
            'city': widgets.TextInput(attrs={'placeholder': 'Paris'}),
            'zip_code': widgets.TextInput(attrs={'placeholder': '59120'})
        }
