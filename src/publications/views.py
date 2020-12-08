
from django.shortcuts import get_object_or_404, render
from taggit.models import Tag
from django.contrib import messages
from django.db.models import Count

from .models import Post, Comment, Category
from .forms import CommentForm
from .services import (filter_post_by_tag, filter_post_by_category,
                       add_new_comment_to_post, posts_pagination)


def post_list(request, tag_slug=None, category_slug=None):
    """
    A web service displaying all published posts.
    Веб-сервис, отображающих все опубликованные посты.
    """
    post = Post.published.all()
    post, tag = filter_post_by_tag(tag_slug, post)
    post, category = filter_post_by_category(category_slug, post)
    page, posts = posts_pagination(post, 3, request)

    return render(request, 'publications/list.html', {'page': page,
                                                      'posts': posts,
                                                      'tag': tag,
                                                      'category': category})


def post_detail(request, year, month, day, slug):
    """
    A web service that displays the post.
    Веб-сервис, отображающий пост.
    """
    post = get_object_or_404(Post, slug=slug, status='published',
                             date_published__year=year,
                             date_published__month=month,
                             date_published__day=day)
    comments = post.publications_comments.filter(moderation=True)
    new_comment, comment_form = add_new_comment_to_post(request, post)

    return render(request, 'publications/detail.html',
                           {'post': post,
                            'comments': comments,
                            'new_comment': new_comment,
                            'comment_form': comment_form})
