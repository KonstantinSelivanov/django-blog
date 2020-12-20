from django.shortcuts import get_object_or_404, render
from django.db.models import Q, F
from django.contrib.sessions.models import Session

from .models import Post, About, Contact
from .services import (add_new_comment_to_post, filter_post_by_category,
                       filter_post_by_tag, get_similar_posts,
                       paginate_posts_page, send_feedback)


def post_list(request, tag_slug=None, category_slug=None):
    """
    Show all posts published.
    Отобразить все опубликованные посты.
    """
    post = Post.published.all()
    
    post, tag = filter_post_by_tag(tag_slug, post)
    post, category = filter_post_by_category(category_slug, post)
    page, posts = paginate_posts_page(post, 3, request)

    return render(request, 'publications/list.html', {'page': page,
                                                      'posts': posts,
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
    similar_posts = get_similar_posts(post, 4)

    # print(request.session)
    # if requests.session.get('has_commented', False):
    #     Post.published.filter(pk=post.id).update(number_of_views=F('number_of_views'))
    # Post.published.filter(pk=post.id).update(number_of_views=F('number_of_views') + 1)
    # request.session['has_commented'] = True
    return render(request, 'publications/detail.html',
                           {'post': post,
                            'comments': comments,
                            'new_comment': new_comment,
                            'comment_form': comment_form,
                            'similar_posts': similar_posts})


def display_page_about_blog(request):
    """
    Display the blog information page.
    Отобразить страницу с информацией о блоге.
    """
    about = get_object_or_404(About)

    return render(request, 'publications/about.html', {'about': about})


def display_page_contact(request):
    """
    Display a page with contacts, as well as a feedback form with
    a blog author.
    Отобразить страницу с контактами, а также форму обратной связи
    с автором блога.
    """
    contact = get_object_or_404(Contact)
    feedback_form = send_feedback(request)

    return render(request, 'publications/contact.html',
                           {'contact': contact,
                            'feedback_form': feedback_form})


def search(request):
    """
    Search blog posts.
    Поиск постов блога.
    """
    search_query = request.GET.get('search', '')
    object_list = Post.published.filter(
        Q(title__icontains=search_query) | Q(body__icontains=search_query))
    page, posts = paginate_posts_page(object_list, 3, request)

    return render(request, 'publications/list.html',
                           {'page': page, 'posts': posts})
