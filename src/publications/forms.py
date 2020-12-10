from django import forms
from captcha.fields import CaptchaField

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Comment form
    Форма комментариев
    """
    captcha = CaptchaField(label='Вы точно человек?')

    class Meta:
        model = Comment
        fields = ('author', 'email', 'body')
