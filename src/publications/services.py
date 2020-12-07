from typing import Union
from django.shortcuts import get_object_or_404
from taggit.models import Tag


def filter_post_by_tag(tag_slug, post) -> Union[list, str]:
    """
    Filter blog posts by tag.
    Фильтрация постов блога по тегу.
    """
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post = post.filter(tags__in=[tag])
    return post, tag
