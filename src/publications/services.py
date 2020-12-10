from typing import Union
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django import template
from django.db.models import Count

from .models import Comment, Category, Post
from .forms import CommentForm
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def filter_post_by_tag(tag_slug: str, post: list) -> Union[list, str]:
    """
    Filter blog posts by tag.
    Фильтрация постов блога по тегу.
    """
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post = post.filter(tags__in=[tag])
    return post, tag



def filter_post_by_category(category_slug: str,
                            post: list) -> Union[list, str]:
    """
    Filter blog posts by category.
    Фильтрация постов блога по категории.
    """
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category__in=[category])
    return post, category


def paginate_posts_page(post: list,
                        number_of_post: int,
                        request) -> Union[list, str]:
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


def get_similar_posts(post: list, count_post: int) -> list:
    """
    Get a list of related articles by tags.
    Получение списка похожих статей по тегам.
    """
    # Formation of a list of related posts by tags
    # Getting all the current post ID tags. Getting a flat list - flat=True
    # Формирование списка похожих статей по тегам. Получение всех ID тегов
    # текущей статьи. Получение плоского списка - flat=True
    post_tags_ids = post.tags.values_list('id', flat=True)
    # Getting all the stations that are associated with at least one tag,
    # excluding the current post.
    # Получение всех статьей, которые связаны хотя бы с одним тегом,
    # исключая текущую статью.
    similar_posts = Post.published.filter(tags__in=post_tags_ids).\
        exclude(id=post.id)
    # Sort the result by the number of tag matches. If two or more posts have
    # the same set of tags, choose the one that is the newest. Limit the
    # selection to the number of posts that we want to display
    # in the featured list. [:4]
    # Сортировка результата по количеству совпадений тегов. Если две и более
    # статьи имеют одинаковый набор тегов, выбирать ту из них, которая является
    # самой новой. Ограничить выборку тем количеством статей, которое мы хотим
    # отображать в списке рекомендуемых. [:4]
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).\
        order_by('-same_tags', '-date_published')[:count_post]
    return similar_posts


def add_new_comment_to_post(request,
                            post: list) -> Union[Comment, CommentForm]:
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
           # human = True # captcha
            new_comment.save()
            messages.success(request, 'Коментарий успешно добавлен')
        else:
            messages.error(request, comment_form.errors)
    else:
        comment_form = CommentForm()
    return new_comment, comment_form
