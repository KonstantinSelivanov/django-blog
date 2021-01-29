from config import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

from .forms import FeedbackForm


def send_feedback(request) -> FeedbackForm:
    """
    Send feedback.
    Оставить сообщение.
    """
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            subject = feedback_form.cleaned_data['subject']
            email = feedback_form.cleaned_data['email']
            message = feedback_form.cleaned_data['message']

            recipient_list = [settings.EMAIL_HOST_USER]
            recipient_list.append(email)

            try:
                send_mail(subject, message, [settings.EMAIL_HOST_USER],
                          recipient_list)
            except BadHeaderError:
                return HttpResponse('Обнаружен недопустимый заголовок')

            messages.success(request, 'Сообщение отправлено')
            feedback_form = FeedbackForm()
        else:
            messages.error(request, 'Ошибка заполениния формы обратной связи')
    else:
        feedback_form = FeedbackForm()

    return feedback_form
