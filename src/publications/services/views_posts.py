from typing import Union

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, F, Q

from ..models import Post, Visitor
from .sessions import get_ip_address, get_session_key, get_user_agent


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


def get_count_number_of_views_post(request, post: list) -> None:
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
