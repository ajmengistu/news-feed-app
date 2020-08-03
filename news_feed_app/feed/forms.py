from django import forms
# from django.db import models 
# from django.forms import ModelForm


from .models import *

class CategoryForm(forms.Form):
    sports = forms.BooleanField(required=False, initial=False)
    general = forms.BooleanField(required=False, initial=True)
    business = forms.BooleanField(required=False, initial=False)
    entertainment = forms.BooleanField(required=False, initial=False)
    health = forms.BooleanField(required=False, initial=False)
    science = forms.BooleanField(required=False, initial=False)
    technology = forms.BooleanField(required=False, initial=False)