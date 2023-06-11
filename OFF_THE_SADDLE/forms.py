from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form to add a comment from the user.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            "body": "Share your climb experience here.",
        }


class EditForm(forms.ModelForm):
    """
    Form to edit a comment from the user.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            "body": "Edit your ride information below:",
        }