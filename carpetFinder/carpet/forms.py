from django import forms

from .models import Carpet

class NewCarpetForm(forms.ModelForm):
    class Meta:
        model = Carpet
        fields = ('name', 'description', 'price', 'size', 'material', 'style', 'color', 'suitability', 'image', 'location')
        widgets = {
            'name': forms.TextInput(),
            'description': forms.Textarea(),
            'price': forms.TextInput(),
            'style': forms.Select(),
            'color': forms.Select(),
            'suitability': forms.Select(),
            'material': forms.Textarea(),
            'image': forms.FileInput(),
            'location': forms.TextInput(),
        }

class EditCarpetForm(forms.ModelForm):
    class Meta:
        model = Carpet
        fields = ('name', 'description', 'price', 'size', 'material', 'style', 'color', 'suitability', 'image', 'is_sold', 'location')
        widgets = {
            'name': forms.TextInput(),
            'description': forms.Textarea(),
            'price': forms.TextInput(),
            'style': forms.Select(),
            'color': forms.Select(),
            'suitability': forms.Select(),
            'material': forms.Textarea(),
            'image': forms.FileInput(),
            'location': forms.TextInput(),
        }