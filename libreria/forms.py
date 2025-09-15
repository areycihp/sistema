from django import forms
from .models import Libro

#Declaracion de formulario
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

