from django import template
from django.db.models import Count

from ..models import Category, Post


register = template.Library()


@register.simple_tag(name='total_posts')
def total_posts():
    """
    Returns the number of posts published.
    Возвращает количество опубликованных постов.
    """
    return Post.published.count()


@register.inclusion_tag('publications/latest_posts.html')
def show_latest_posts(count: int):
    """
    Displays recent blog posts.
    Отображает последние посты блога.
    """
    latest_posts = Post.published.order_by('-date_published')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag(name='get_most_commented_posts')
def get_most_commented_posts(count=5):
    """
    Displays a list of articles with the most comments. The annotate() method
    is used to add the number of comments to each article. Sorting the result
    by the number of comments.
    Отображет список статей с наибольшим количеством комментариев.
    Метод annotate() служит для добавления к каждой статье количества ее
    комментариев. Сортировка результата по количеству комментариев.
    """
    return Post.published.annotate(
        total_comments=Count('publications_comments')).\
        order_by('-total_comments')[:count]


@register.inclusion_tag('publications/category.html')
def show_list_category():
    """
    Displays blog posts by category.
    Отображает посты блога по категориям.
    """
    cat_posts = Category.category_manager.all()
    # print(cat_posts)
    return {'cat_posts': cat_posts}


@register.inclusion_tag('publications/archives.html')
def render_month_links():
    return {
        'all_posts': Post.published.order_by('date_published'),
    }
