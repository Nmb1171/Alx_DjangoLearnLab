from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget


class PostForm(forms.ModelForm): 
    class Meta: model = Post 
    fields = ['title', 'content', 'tags']
    widgets = { 
            'tags': TagWidget(),
            } 


    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("The title must be at least 5 characters long.")
        return title

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only include the content field

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or len(content.strip()) == 0:
            raise forms.ValidationError("Comment cannot be empty.")
        return content

