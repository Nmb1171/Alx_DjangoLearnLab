from django import forms
from bookshelf.models import CustomUser

class CustomUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput (attrs={'type':'date'}),    
        }
       
       
        labels = {
            'username':'Your Username', 
            'email':'Your Email Address',
            'date_of_birth': 'Your Date Of Birth'
        }


        help_texts = {
            'username': 'Enter a unique username.',
        }


        