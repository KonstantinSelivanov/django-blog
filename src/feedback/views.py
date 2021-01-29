from django.shortcuts import render

from .services import send_feedback

def feedback(request):
    """
    Display a page with contacts, as well as a feedback form with
    a blog author.
    Отобразить страницу с контактами, а также форму обратной связи
    с автором блога.
    """
    feedback_form = send_feedback(request)
    return render(request, 'feedback/contact.html',
                           {'feedback_form': feedback_form})