from django import forms
from captcha.fields import CaptchaField
from ckeditor.widgets import CKEditorWidget

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Comment form
    Форма комментариев
    """
    body = forms.CharField(label='Сообщение',
                           widget=CKEditorWidget())
    captcha = CaptchaField(label='Вы точно человек?')

    class Meta:
        model = Comment
        fields = ('author', 'email')


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
                              widget=CKEditorWidget())

    captcha = CaptchaField(label='Вы точно человек?')
