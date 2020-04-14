from django.forms import Form, ModelForm, ValidationError
from django.forms.fields import CharField, IntegerField
from django.forms.widgets import TextInput


class CreateProductForm(Form):
    name = CharField(widget=TextInput(attrs={'placeholder': 'Name'}))
    surname = CharField(widget=TextInput(attrs={'placeholder': 'Surname'}))

    def clean(self):
        name = self.cleaned_data['name']
        if name == 'Eugenie Bouchard':
            # self.add_error('name', 'Eugenie Bouchard is not allowed there')
            raise ValidationError('Eugenie Bouchard is not allowed here')
        return super().clean()
    
class CreateProductFormII(Form):
    price = IntegerField(widget=TextInput(attrs={'placeholder': 'Price'}))


class FormSelector:
    """"A class that allows to select multiple different
    forms for a same given view"""
    def __init__(self, *forms, request=None, max_steps=1):
        self.request = request
        self.max_steps = max_steps
        self.context = {'final_step': False}
        self.forms = [CreateProductForm, CreateProductFormII]

    @property
    def url(self):
        return self.get_context()['url']

    @property
    def get_request(self):
        return self.request

    def is_final_step(self, step):
        return self.max_steps == step

    def get_context(self):
        # Get the current step in the
        # creation process
        current_step = self.request.GET.get('step')
        # We can assume that if there is no step,
        # we are starting a step n°1
        if current_step is None or current_step == '':
            current_step = 1

        if isinstance(current_step, str):
            current_step = int(current_step)

        next_step = current_step + 1

        # When the number of steps does not correspond
        # to the number of forms, we have a problem
        if self.max_steps != len(self.forms):
            return {'form': {}, 'error': 'The number of steps and the forms do not correpond'}

        try:
            form = self.forms[current_step - 1]
        except:
            form = self.forms[0]
        else:
            self.context.update({'form': form})

        # Immediately check if the user has cheated
        # and started at step n°2. In that case,
        # just return a context without proceeding
        # if current_step > 1:
        #     has_started_process = self.request.session['has_started_process']
        #     if not has_started_process:
        #         self.context.update({'form': self.forms[0], 'url': self._get_redirect_url('create', 1)})
        #         return self.context
        
        # Once the user has passed the first step,
        # then we register the creation process
        # if current_step == 2:
        #     self.request.session['has_started_process'] = True

        # All time the max_steps has not been
        # reached, just redirect to the next steps
        if current_step < self.max_steps:
            self.context.update({'url': self._get_redirect_url('create', next_step)})
            return self.context

        # Also check if we have no reached
        # the maximum amount of steps
        if current_step == self.max_steps:
            self.context.update({'url': self._get_final_url('list_items'), 'final_step': True})
            return self.context
        
    def _get_final_url(self, name):
        from django.shortcuts import reverse
        return reverse(name)

    def _get_redirect_url(self, name, step):
        from django.shortcuts import reverse
        return reverse(name) + f'?step={step}'

    def post(self, request, instance=None):
        """Posts the request data in the selected form"""
        try:
            form = self.get_context()['form']
        except:
            return None
        else:
            if instance:
                f = form(request.POST, instance=instance)
            else:
                f = form(request.POST)
            if f.is_valid():
                # f.save()
                return True
            else:
                return False
