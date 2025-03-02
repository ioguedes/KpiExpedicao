from django import forms
from .models import Carregamento

class CarregamentoForm(forms.ModelForm):
    class Meta:
        model = Carregamento
        fields = '__all__'