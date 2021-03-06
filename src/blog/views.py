from django.shortcuts import get_object_or_404, render
from django.views.generic.dates import MonthArchiveView

from .models import Post
from .services import (filter_post_by_category, filter_post_by_tag, search,
                       get_count_number_of_views_post, get_similar_posts,
                       paginate_posts_page, add_new_comment_to_post)


def post_list(request, tag_slug=None, category_slug=None):
    """
    Show all posts published.
    Отобразить все опубликованные посты.
    """
    posts = Post.published.all()

    posts = search(request, posts)
    posts, tag = filter_post_by_tag(tag_slug, posts)
    posts, category = filter_post_by_category(category_slug, posts)
    pages = paginate_posts_page(posts, 3, request)

    return render(request, 'blog/post_list.html',
                           {'object_list': pages,
                            'tag': tag,
                            'category': category})


def post_detail(request, year, month, day, slug):
    """
    Show details of published post.
    Отобразить детали опубликованного поста.
    """
    post = get_object_or_404(Post, slug=slug, status='published',
                             date_published__year=year,
                             date_published__month=month,
                             date_published__day=day)

    comments = post.publications_comments.filter(moderation=True)
    new_comment, comment_form = add_new_comment_to_post(request, post)
    similar_posts = get_similar_posts(post, 2)
    get_count_number_of_views_post(request, post)

    return render(request, 'blog/post_detail.html',
                           {'post': post,
                            'comments': comments,
                            'new_comment': new_comment,
                            'comment_form': comment_form,
                            'similar_posts': similar_posts})


class PostMonthArchiveView(MonthArchiveView):
    """
    Displaying the archive of posts. Context_processors is connected.
    Отображение архива постов. Подключен context_processors.
    """
    queryset = Post.published.all()
    date_field = 'date_published'
    allow_future = True
    template_name = 'blog/post_list.html'
