from django import forms
from .models import Comentario

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
