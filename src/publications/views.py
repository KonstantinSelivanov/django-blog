from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Post


def post_list(request):
    """
    A web service displaying all published posts.
    Веб-сервис, отображающих все опубликованные посты.
    """
    post = Post.published.all()
    paginator = Paginator(post, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'publications/list.html', {'page': page,
                                                      'posts': posts})


def post_detail(request, year, month, day, slug):
    """
    
    """
    post = get_object_or_404(Post, slug=slug, status='published',
                             date_published__year=year,
                             date_published__month=month,
                             date_published__day=day)


    return render(request, 'publications/detail.html', {'post': post})
