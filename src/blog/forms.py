from captcha.fields import CaptchaField
from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Comment form
    Форма комментариев
    """
    body = forms.CharField(label='Сообщение',
                           widget=CKEditorWidget(config_name='user'))
    captcha = CaptchaField(label='Вы точно человек?')

    class Meta:
        model = Comment
        fields = ('author', 'email', 'body')
