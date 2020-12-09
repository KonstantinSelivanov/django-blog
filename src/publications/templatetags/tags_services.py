from django import template

from ..models import Post, Category


# A module-level variable named register, which is an instance
# of template.Library in which all tags and filters are registered.
# Переменна уровня модуля с именем register, которая является экземпляром
# template.Library, в котором зарегистрированы все теги и фильтры.
register = template.Library()


@register.simple_tag(name='total_posts')
def total_posts():
    """
    Returns the number of posts published.
    Возвращает количество опубликованных постов.
    """
    return Post.published.count()


@register.inclusion_tag('publications/latest_posts.html')
def show_latest_posts(count: int):
    """
    Display tag for recent blog posts
    Тег отображения последних статей блога
    """
    latest_posts = Post.published.order_by('-date_published')[:count]
    return {'latest_posts': latest_posts}
