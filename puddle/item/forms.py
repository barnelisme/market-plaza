from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Itemfields = ('category','name', 'description', 'price', 'image',)
