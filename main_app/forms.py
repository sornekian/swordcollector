from django.forms import ModelForm
from .models import Sword

class SwordForm(ModelForm):
  class Meta:
    model = Sword
    fields = ['category', 'age', 'blade_material', 'blade_length']