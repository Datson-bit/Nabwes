from django import forms
from .models import Comment, Registration

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['text', 'email', 'author']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model= Registration
        fields= ['full_name', 'email', 'phone']