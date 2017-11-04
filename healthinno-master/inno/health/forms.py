
from django import forms

class docd(forms.Form):
    initial_date = forms.DateField()
    final_date = forms.DateField()
