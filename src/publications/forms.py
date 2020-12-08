from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Comment form
    Форма комментариев
    """

    class Meta:
        model = Comment
        fields = ('author', 'email', 'body')
