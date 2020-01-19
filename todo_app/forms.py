from django import forms
from .models import List

class ListForm(forms.ModelForm):
    class meta:
    	model=List
    	fields=["item","completed"]
