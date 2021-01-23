from django import forms
from .models import Project, Profile, Review

class projectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['developer']
        widgets = {
            'description': forms.Textarea(
                attrs={'placeholder': 'add description', 'rows': 2}),
                
        }  