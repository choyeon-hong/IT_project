from typing import Any
from django import forms
# from wandercritic.models import Page, Category
from django.contrib.auth.models import User
# from wandercritic.models import UserProfile

# class CategoryForm(forms.ModelForm):
#     name = forms.CharField(max_length=Category.NAME_MAX_LENGTH, help_text="Please enter the category name.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0) 
#     #the fields will be hidden, the user won’t be able to enter a value for these fields
#     likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     slug = forms.CharField(widget=forms.HiddenInput(), required=False)

#     class Meta:
#         model = Category
#         fields = ('name',) #specify the fields to include from the form

# class PageForm(forms.ModelForm):
#     title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH, help_text="Please enter the title of the page.")
#     url = forms.URLField(max_length=Page.URL_MAX_LENGTH, help_text="Please enter the URL of the page.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
#     class Meta:
#         model = Page
#         exclude = ('category',) #excludes from the form

#     def clean(self) :
#         cleaned_data = self.cleaned_data
#         url = cleaned_data.get('url')
#         # If url is not empty and doesn't start with 'http://',
#         # then prepend 'http://'.
#         if url and not url.startswith('http://'):
#             url = f'http://{url}'
#             cleaned_data['url'] = url
#         return cleaned_data
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('website', 'picture',)