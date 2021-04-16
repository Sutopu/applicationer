from django import forms
from .models import Application

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
