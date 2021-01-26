from django import forms
from django.conf import settings
from tinymce.widgets import TinyMCE
from captcha.fields import CaptchaField

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Comment form
    Форма комментариев
    """
    body = forms.CharField(label='Сообщение',
                           widget=TinyMCE(mce_attrs=settings.TINYMCE_USER))
    captcha = CaptchaField(label='Вы точно человек?')

    class Meta:
        model = Comment
        fields = ('author', 'email', 'body')
