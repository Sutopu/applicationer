from django import forms
from .models import Application
from django.forms import ModelForm, TextInput

class AddApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'company',
            'role',
            'level',
            'pay',
            'benefits',
            'location',
            'notes',
            'status',
        ]