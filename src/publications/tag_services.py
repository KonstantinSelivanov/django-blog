from django import template

from .models import Post
from django.shortcuts import get_object_or_404
from taggit.models import Tag


# A module-level variable named register, which is an instance
# of template.Library in which all tags and filters are registered.
# Переменна уровня модуля с именем register, которая является экземпляром
# template.Library, в котором зарегистрированы все теги и фильтры.
register = template.Library()

# Decorator for registering a new tag
# Декоратор для регистрации нового тега
@register.tag(name='total_posts')
def total_posts():
    # Returns the number of posts published
    # Возвращает количество опубликованных постов
    return Post.published.count()


def filter_post_by_tag(tag_slug, post):
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post = post.filter(tags__in=[tag])
    return post, tag