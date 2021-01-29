from django import forms
from ckeditor.widgets import CKEditorWidget
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
                              widget=CKEditorWidget(config_name='user'))
    captcha = CaptchaField(label='Вы точно человек?')
