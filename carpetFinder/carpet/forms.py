from django import forms

from .models import Carpet

style = 'w-full py-4 px-6 rounded-xl border'

class NewCarpetForm(forms.ModelForm):
    class Meta:
        model = Carpet
        fields = ('name', 'description', 'price', 'size', 'material', 'style', 'color', 'suitability', 'image', 'location')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': style
            }),
            'description': forms.Textarea(attrs={
                'class': style
            }),
            'price': forms.TextInput(attrs={
                'class': style
            }),
            'style': forms.Select(attrs={
                'class': style
            }),
            'color': forms.Select(attrs={
                'class': style
            }),
            'suitability': forms.Select(attrs={
                'class': style
            }),
            'material': forms.Textarea(attrs= {
                'class': style
            }),
            'image': forms.FileInput(attrs={
                'class': style
            }),
            'location': forms.TextInput(attrs={
                'class': style
            }),
        }

class EditCarpetForm(forms.ModelForm):
    class Meta:
        model = Carpet
        fields = ('name', 'description', 'price', 'size', 'material', 'style', 'color', 'suitability', 'image', 'is_sold', 'location')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': style
            }),
            'description': forms.Textarea(attrs={
                'class': style
            }),
            'price': forms.TextInput(attrs={
                'class': style
            }),
            'style': forms.Select(attrs={
                'class': style
            }),
            'color': forms.Select(attrs={
                'class': style
            }),
            'suitability': forms.Select(attrs={
                'class': style
            }),
            'material': forms.Textarea(attrs= {
                'class': style
            }),
            'image': forms.FileInput(attrs={
                'class': style
            }),
            'location': forms.TextInput(attrs={
                'class': style
            }),
        }