from django import forms
from .models import Comment, RideTime


class CommentForm(forms.ModelForm):
    """
    Form to add ride statistics to the blog post from the user.
    Includes a field for ride time and custom comments.
    """
    # ride_time = forms.DurationField(required=False, label='Ride Time')

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
            "body": "Make updates to your ride information below:",
        }
