from django import forms
from . models import my_table

class my_form(forms.ModelForm):
    class Meta:
        model=my_table
        fields=['no','name']
        widgets={'no':forms.NumberInput(),'name':forms.TextInput()}