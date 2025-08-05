from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile

class RegistrationForm(forms.ModelForm):
      
      username = forms.CharField(max_length=30, required=True , help_text='' , widget=forms.TextInput(attrs={"ftype":"text" ,"class":"form-control", "id":"username", "name":"username" }))
      first_name = forms.CharField(max_length=30, required=True , help_text='' , widget=forms.TextInput(attrs={"ftype":"text" ,"class":"form-control", "id":"first_name", "name":"first_name"}))
      last_name = forms.CharField(max_length=30, required=True , help_text='' , widget=forms.TextInput(attrs={"ftype":"text" ,"class":"form-control", "id":"last_name", "name":"last_name"}))
      email = forms.EmailField(max_length=254, help_text='' , widget=forms.EmailInput(attrs={"ftype":"email" ,"class":"form-control", "id":"email", "name":"email"}))
      password = forms.CharField(max_length=30, required=True , help_text='' , widget=forms.PasswordInput(attrs={"ftype":"password" ,"class":"form-control", "id":"password", "name":"password"}))
      confirm_password = forms.CharField(max_length=30, required=True , help_text='' , widget=forms.PasswordInput(attrs={"ftype":"password" ,"class":"form-control", "id":"confirm_password", "name":"confirm_password"}))
      photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
      class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
       
        

class UserEditForm(forms.ModelForm):
  class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ProfileEditForm(forms.ModelForm):
  class Meta:
        model = Profile
        fields = ['bio', 'date_of_birth', 'photo']
        widgets = {
           
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control ', 'type': 'date'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            
        }