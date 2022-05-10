from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    
    document = forms.CharField(label='Document', widget=forms.IntegerField)
    documentType = forms.ChoiceField(label='Document Type')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput)
    birthday = forms.CharField(label='Birthday', widget=forms.DateField)

    class Meta:
        model = User
        fields = ['document', 'documentType', 'last_name', 'email', 'username', 'password1', 'password2']
        help_texts = {k:"" for k in fields}