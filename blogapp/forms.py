from django import forms
from blogapp.models import Comments, Post

class CommentsForm(forms.ModelForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Nom d\'utilisateur'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control' , 'placeholder': 'Email'}))
  body = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': ' Votre commentaire'}))
  class Meta:
    model = Comments
    fields = ['username', 'email', 'body']
   

class SearchPost(forms.Form):
  query = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Search'}))

  class Meta:
    fields = ['query']
    
class PostForm(forms.ModelForm):
  
  title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Titre'}))
  body = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Votre article'}))
  image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control' , 'placeholder': 'Image'}))
 
  class Meta:
    model = Post
    fields = ['title', 'body', 'image']


