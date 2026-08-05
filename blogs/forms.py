from django import forms

from blogs.models import Blogs

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title', 'content',)