from django import forms
from captcha.fields import CaptchaField
from ckeditor.widgets import CKEditorWidget


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
