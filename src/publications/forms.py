from django import forms
from captcha.fields import CaptchaField
from tinymce.widgets import TinyMCE

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Comment form
    Форма комментариев
    """
    body = forms.CharField(label='Сообщение', widget=TinyMCE())
    captcha = CaptchaField(label='Вы точно человек?')

    class Meta:
        model = Comment
        fields = ('author', 'email', 'body')
