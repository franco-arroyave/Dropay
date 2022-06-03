from cProfile import Profile
from tkinter import Widget
from urllib import request
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import TypeID, Profile

class UserRegisterForm(UserCreationForm):
    
    
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    last_name = forms.CharField(required=True)
    

    class Meta:
        model = User
        fields = ['first_name', 
        'last_name', 
        'email', 
        'username', 
        'password1', 
        'password2']

        help_texts = {k:"" for k in fields}

    def clean(self):
        super(UserRegisterForm, self).clean()

        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            
           if self.cleaned_data['password1'] != self.cleaned_data['password2']:
               raise forms.ValidationError("Passwords don't match each other")



class ProfileRegisterForm(forms.ModelForm):
   
    IdentityDocument = forms.CharField(label='Document', widget=forms.NumberInput)
    TypeID = forms.ModelChoiceField(empty_label='Document Type', queryset=TypeID.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    DataPolicy = forms.BooleanField()

    class Meta:
        model = Profile
        fields = ['IdentityDocument', 
        'TypeID', 
        'DataPolicy']

        help_texts = {k:"" for k in fields}

    def clean(self):
        super(ProfileRegisterForm, self).clean()

        if 'DataPolicy' == 1:
            raise forms.ValidationError("Data policy ir required")

            

            
class updateUserForm(forms.ModelForm):

    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    last_name = forms.CharField(required=True)
    

    class Meta:
        model = User
        fields = ['first_name', 
        'last_name', 
        'email', 
        'password1', 
        'password2']

        help_texts = {k:"" for k in fields}

    def clean(self):
        super(UserRegisterForm, self).clean()

        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            
           if self.cleaned_data['password1'] != self.cleaned_data['password2']:
               raise forms.ValidationError("Passwords don't match each other")

            