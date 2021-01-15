from django.shortcuts import get_object_or_404, render

from .models import About, Contact
from .services import send_feedback


def display_page_about_blog(request):
    """
    Display the blog information page.
    Отобразить страницу с информацией о блоге.
    """
    about = get_object_or_404(About)
    return render(request, 'pages/about.html', {'about': about})


def display_page_contact(request):
    """
    Display a page with contacts, as well as a feedback form with
    a blog author.
    Отобразить страницу с контактами, а также форму обратной связи
    с автором блога.
    """
    contact = get_object_or_404(Contact)
    feedback_form = send_feedback(request)
    return render(request, 'pages/contact.html',
                           {'contact': contact,
                            'feedback_form': feedback_form})
