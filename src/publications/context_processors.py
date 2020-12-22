from .models import Post


def posts(request):
    return {
            'all_posts': Post.published.order_by('date_published'),
           }
