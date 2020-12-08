from typing import Union
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django import template

from .models import Comment, Category
from .forms import CommentForm
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



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


def filter_post_by_category(category_slug, post) -> Union[list, str]:
    """
    Filter blog posts by category.
    Фильтрация постов блога по категории.
    """
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category__in=[category])
    return post, category


def posts_pagination(post, number_of_post: int, request) -> Union[list, str]:
    """
    Blog post pagination
    Пагинация постов блога
    """
    paginator = Paginator(post, number_of_post)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return page, posts


def add_new_comment_to_post(request, post) -> Union[Comment, CommentForm]:
    """
    Add new comment to post
    Добавление нового комментария к посту
    """
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Коментарий успешно добавлен')
        else:
            messages.error(request, comment_form.errors)
    else:
        comment_form = CommentForm()
    return new_comment, comment_form
