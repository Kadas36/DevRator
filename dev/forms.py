from django import forms
from .models import Project, Profile, Review

class projectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['developer']
        widgets = {
            'title': forms.Textarea(
                attrs={'placeholder': 'add description', 'rows': 1}),
            'description': forms.Textarea(
                attrs={'placeholder': 'add description', 'rows': 2}),    
                
        }  

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []
        widgets = {
            'bio': forms.Textarea(
                attrs={'placeholder': 'add description', 'rows': 2}),

            'user': forms.TextInput(
                attrs={'readonly':'readonly'}),   
                
        }  


class reviewForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['reviewer', 'project']
        widgets = {
            'comment': forms.Textarea(
                attrs={'placeholder': 'add description', 'rows': 2}),                
        }       



