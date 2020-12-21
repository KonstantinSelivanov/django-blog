from django.shortcuts import get_object_or_404, render
from django.db.models import Q, F
from django.contrib.sessions.models import Session

from .models import Post, About, Contact, Visitor
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

import re
# this is not intended to be an all-knowing IP address regex
IP_RE = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

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
    
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR',
                                  request.META.get('REMOTE_ADDR', '127.10.0.1'))
    if ip_address:
        # make sure that only one IP
        # убедиться что только один IP
        try:
            ip_address = IP_RE.match(ip_address)
            if ip_address:
                ip_address = ip_address.group(0)
            else:
                # нет IP, вероятно, от какого-то прокси или другого устройства
                # на каком-то поддельном IP
                # no IP, probably from some proxy or other device
                # in some bogus IP
                ip_address = '10.0.0.1'
        except IndexError:
            pass

    user_agent = request.META.get('HTTP_USER_AGENT', '')[:255]

    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key

    obj1 = Visitor.objects.filter(Q(session=session_key) & Q(post_id=post.id))

    if obj1.exists():
        pass
    else:
        Post.published.filter(pk=post.id).update(hits=F('hits') + 1)

    Visitor(session=session_key,
            ip=ip_address,
            user_agent=user_agent,
            post_id=post.id).save()

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
