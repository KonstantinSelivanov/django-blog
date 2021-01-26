from django import forms
from django.conf import settings

from tinymce.widgets import TinyMCE
from captcha.fields import CaptchaField


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
                              widget=TinyMCE(mce_attrs=settings.TINYMCE_USER))
    captcha = CaptchaField(label='Вы точно человек?')
