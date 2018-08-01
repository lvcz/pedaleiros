from django import forms
from .models import Ciclistas


class CiclistasForm(forms.ModelForm):
    # id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sexo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    data_de_nascimento = forms.DateField(widget=forms.DateField(attrs={'class':'form-control'}))
    data_de_inscricao = forms.DateField(widget=forms.DateField(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    senha = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Ciclistas
        fields = ['Nome', 'Sexo', 'Data de Nascimento', 'Email', 'Senha']
