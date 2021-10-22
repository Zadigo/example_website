import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_date_of_birth(instance):
    current_year = timezone.now().year
    age = current_year - instance.year
    if age < 18:
        raise ValidationError('Age is not valid')
    return instance
