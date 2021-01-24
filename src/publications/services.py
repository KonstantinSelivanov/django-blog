import re
from typing import Union


from django.contrib.messages.api import debug

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, F, Q


from django.shortcuts import get_object_or_404
from taggit.models import Tag

from .forms import CommentForm
from .models import Category, Comment, Post, Visitor


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


def paginate_posts_page(posts: list,
                        number_of_post: int,
                        request) -> Union[list, str]:
    """
    Blog post pagination
    Пагинация постов блога
    """
    paginator = Paginator(posts, number_of_post)
    page = request.GET.get('page')
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return pages


def get_similar_posts(post: list, count_post: int) -> list:
    """
    Get a list of related articles by tags.
    Получить список похожих статей по тегам.
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
    Add a new comment to the post.
    Добавить новый комментарий к посту.
    """
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            Post.published.filter(pk=post.id).update(comments=F('comments') + 1)
            comment_form = CommentForm()
        else:
            debug(request, comment_form.errors)
    else:
        comment_form = CommentForm()
    return new_comment, comment_form


def search(request, posts: list) -> list:
    """
    Search blog posts.
    Поиск постов блога.
    """
    search_query = request.GET.get('search', '')
    if search_query:
        # List of objects filtered by search_query. Filter \ search for
        # articles by title and content.
        # Список объектов отфильтрованных с помошью поискового
        # запроса search_query. Фильтр\поиск статей осуществляется
        # по заголовку и содержимому.
        posts = Post.published.filter(
            Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        # Object all list
        # Список всех объектов
        posts = Post.published.all()
    return posts


def get_ip_address(request) -> str:
    """
    Get the visitor's IP address.
    Получить IP адрес посетителя.
    """
    # A regular expression pattern for an IP address.
    # Шаблон регулярного выражения для IP адреса.
    # flake8: noqa W605
    IP_RE = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

    ip_address = request.META.get(
        'HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '127.10.0.1'))
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
    return ip_address


def get_user_agent(request) -> str:
    """
    Get information about the visitor's browser.
    Получить информацию о браузере посетителя.
    """
    user_agent = request.META.get('HTTP_USER_AGENT', '')[:255]
    return user_agent


def get_session_key(request) -> str:
    """
    Get a visitor session.
    Получить сессию посетителя.
    """
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    return session_key


def count_number_of_views_post(request, post) -> None:
    """
    Counting the number of views of posts.
    Подсчет количества просмотров постов.
    """
    ip_address = get_ip_address(request)
    user_agent = get_user_agent(request)
    session_key = get_session_key(request)

    queryset_visitor = Visitor.objects.filter(
        Q(session=session_key) & Q(post_id=post.id))

    if queryset_visitor.exists():
        pass
    else:
        Post.published.filter(pk=post.id).update(hits=F('hits') + 1)

    Visitor(session=session_key,
            ip=ip_address,
            user_agent=user_agent,
            post_id=post.id).save()
