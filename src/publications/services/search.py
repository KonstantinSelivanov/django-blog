from django.db.models import Q

from ..models import Post


def search(request, posts: list) -> list:
    """
    Search blog posts.
    Поиск постов блога.
    """
    search_query = request.GET.get('search', '')
    if search_query:
        # List of objects filtered by search_query. Filter \ search for
        # articles by title and content.
        # Список объектов отфильтрованных с помошью поискового
        # запроса search_query. Фильтр\поиск статей осуществляется
        # по заголовку и содержимому.
        posts = Post.published.filter(
            Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        # Object all list
        # Список всех объектов
        posts = Post.published.all()
    return posts
