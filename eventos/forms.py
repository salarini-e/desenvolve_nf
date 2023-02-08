from django.forms import ModelForm, ValidationError
from .models import *

class Evento_form(ModelForm):
    class Meta:
        model = Evento
        exclude = []