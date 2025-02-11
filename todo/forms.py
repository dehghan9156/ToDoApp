from django import forms
from .models import ToDo

class ToDoCreateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields=['title']
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control'
            })
        }