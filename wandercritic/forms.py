from typing import Any
from django import forms
from django.contrib.auth.models import User
from .models import Place, PlaceImage, TravelAgentApplication
import json

from allauth.account.forms import LoginForm
class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.
        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)
    

from allauth.account.forms import SignupForm
class MyCustomSignupForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.
        # You must return the original result.
        return user

class PlaceForm(forms.ModelForm):
    highlights = forms.CharField(widget=forms.Textarea, required=False,
                               help_text="Enter each highlight on a new line")
    tips = forms.CharField(widget=forms.Textarea, required=False,
                         help_text="Enter each tip on a new line")
    
    class Meta:
        model = Place
        fields = ['name', 'description', 'short_description', 'location', 
                 'image', 'history', 'highlights', 'best_time_to_visit',
                 'getting_there', 'tips', 'categories', 'tags']
    
    def clean_highlights(self):
        highlights = self.cleaned_data.get('highlights', '')
        if highlights:
            # Convert newline-separated text to JSON list
            highlights_list = [h.strip() for h in highlights.split('\n') if h.strip()]
            return json.dumps(highlights_list)
        return ''
    
    def clean_tips(self):
        tips = self.cleaned_data.get('tips', '')
        if tips:
            # Convert newline-separated text to JSON list
            tips_list = [t.strip() for t in tips.split('\n') if t.strip()]
            return json.dumps(tips_list)
        return ''

class PlaceImageForm(forms.ModelForm):
    class Meta:
        model = PlaceImage
        fields = ['image', 'caption', 'is_primary']

class TravelAgentApplicationForm(forms.ModelForm):
    class Meta:
        model = TravelAgentApplication
        fields = ['full_name', 'company_name', 'experience', 'website', 'phone']
        widgets = {
            'experience': forms.Textarea(attrs={'rows': 5}),
            'website': forms.URLInput(attrs={'placeholder': 'https://'}),
            'phone': forms.TextInput(attrs={'placeholder': '+1234567890'})
        }
        help_texts = {
            'experience': 'Tell us about your experience in the travel industry and why you want to become a travel agent.',
            'company_name': 'If you represent a company, enter its name here.',
            'website': 'Your personal or company website (optional)',
        }