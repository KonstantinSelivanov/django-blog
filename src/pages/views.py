from django.shortcuts import get_object_or_404, render

from .models import About


def display_page_about(request):
    """
    Display the blog information page.
    Отобразить страницу с информацией о блоге.
    """
    about = get_object_or_404(About)
    return render(request, 'pages/about.html', {'about': about})
