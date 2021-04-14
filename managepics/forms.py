from django import forms
from managepics.models import Pic

class ImageForm(forms.ModelForm):
    class Meta:
        model = Pic
        fields = ('name', 'descr', 'pic')