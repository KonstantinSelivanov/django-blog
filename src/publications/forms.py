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
    subject = forms.CharField(label='Тема',
                              max_length=100,
                              widget=forms.TextInput())
    email = forms.EmailField(label='E-mail',
                             max_length=100,
                             widget=forms.TextInput())
    message = forms.CharField(label='Сообщение',
                              widget=forms.Textarea())

    captcha = CaptchaField(label='Вы точно человек?')


class SubscribeForm(forms.Form):
    """
    Subscription form.
    Форма новостной подписки.
    """
    email = forms.EmailField(label='e-mail',
                             max_length=100,
                             widget=forms.EmailInput())