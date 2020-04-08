from django import forms
from .models import Lawnmower, Fertilizer

class LawnmowerForm(forms.ModelForm):
    
    class Meta:
        model = Lawnmower
        fields = ('model', 'brand', 'photo_url',)


class FertilizerForm(forms.ModelForm):
    
    class Meta:
        model = Fertilizer
        fields = ('product', 'description', 'preview_url',)