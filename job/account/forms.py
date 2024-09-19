from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class SignupForm(UserCreationForm):
    # password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class': 'password-toggle','type':'password'}))
    # password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class': 'password-toggle'}))
    class Meta:
        model=User
        fields =['username', 'first_name', 'last_name','email','password1','password2']
    class Media:
        js = ('password_toggle.js', )

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']        

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['city','phone_number','image']        