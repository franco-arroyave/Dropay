from cProfile import Profile
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

    def clean_username(self): # check if username does not exist before
        try:
            User.objects.get(username=self.cleaned_data['username']) #get user from user model
        except User.DoesNotExist :
            return self.cleaned_data['username']

        raise forms.ValidationError("This user exist already choose an0ther username")



    #def clean(self, *args , **kwargs):
    #    super(UserRegisterForm).clean(*args ,**kwargs) # check if password 1 and password2 match each other
    #    if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:#check if both pass first validation
    #        if self.cleaned_data['password1'] != self.cleaned_data['password2']: # check if they match each other
    #            raise forms.ValidationError("Passwords don't match each other")



#class ProfileRegisterForm(forms.ModelForm):
#    
#    document = forms.CharField(label='Document', widget=forms.TextInput)
#    documentType = forms.ModelChoiceField(empty_label='Document Type', queryset=TypeID.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
#    data_policy = forms.CheckboxInput(required=True, widget=forms.CheckboxInput, label='Acept data policy')

#    class Meta:
#        model = Profile
#        fields = ['document', 
#        'documentType', 
#        'data_policy']

#        help_texts = {k:"" for k in fields}