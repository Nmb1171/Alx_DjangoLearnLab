from django import forms
from bookshelf.models import CustomUser


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email Address')
    message = forms.CharField(
        widget=forms.Textarea,
        max_length=500,
        label='Your Message'
    )

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


