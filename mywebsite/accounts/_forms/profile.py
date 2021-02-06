from accounts import custom_widgets
from accounts.models import MyUser, MyUserProfile
from django.forms import ModelForm


class BaseProfileForm(ModelForm):
    class Meta:
        model   = MyUser
        fields  = ['firstname', 'lastname', 'email']
        widgets = {
            'firstname': custom_widgets.FirstNameInput(attrs={'placeholder': 'John'}),
            'lastname': custom_widgets.LastNameInput(attrs={'placeholder': 'Doe'}),
            'email': custom_widgets.TextInput(attrs={'placeholder': 'john.doe@gmail.com'}),
        }


class AddressProfileForm(ModelForm):
    class Meta:
        model   = MyUserProfile
        fields  = ['address', 'city', 'zip_code']
        widgets = {
            'address': custom_widgets.AddressLineOne(attrs={'placeholder': '173 rue de Rivoli'}),
            'city': custom_widgets.TextInput(attrs={'placeholder': 'Paris'}),
            'zip_code': custom_widgets.TextInput(attrs={'placeholder': '59120'})
        }
