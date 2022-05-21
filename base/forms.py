from django.forms import ModelForm
from .models import *

class CreateKitForm(ModelForm):
    class Meta:
        model = Kit
        fields = '__all__'


