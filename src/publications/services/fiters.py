from typing import Union

from django.shortcuts import get_object_or_404
from taggit.models import Tag

from ..models import Category


def filter_post_by_tag(tag_slug: str, posts: list) -> Union[list, str]:
    """
    Filter blog posts by tag.
    Фильтровать посты блога по тегу.
    """
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    return posts, tag


def filter_post_by_category(category_slug: str,
                            posts: list) -> Union[list, str]:
    """
    Filter blog posts by category.
    Фильтровать посты блога по категории.
    """
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category__in=[category])
    return posts, category
