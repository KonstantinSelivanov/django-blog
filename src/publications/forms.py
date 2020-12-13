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


class FeedbackForm(forms.Form):
    """
    Feedback form.
    Форма обратной связи.
    """
    subject = forms.CharField(verbose_name='Имя', max_length=80)
    subject = forms.CharField(verbose_name='Тема', max_length=100)
    email = forms.EmailField(verbose_name='e-mail')
    message = forms.CharField(verbose_name='Сообщение', max_length=500)
    copy = forms.BooleanField(required=False)
