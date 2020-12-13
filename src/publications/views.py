from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.core.mail import send_mail

from .models import Post, About
from .forms import FeedbackForm
from .services import (add_new_comment_to_post, filter_post_by_category,
                       filter_post_by_tag, get_similar_posts,
                       paginate_posts_page)


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

    return render(request, 'publications/detail.html',
                           {'post': post,
                            'comments': comments,
                            'new_comment': new_comment,
                            'comment_form': comment_form,
                            'similar_posts': similar_posts})


def page_about_blog(request):
    """
    Display the blog information page.
    Отобразить страницу с информацией о блоге.
    """
    about = get_object_or_404(About)

    return render(request, 'publications/about.html', {'about': about})


def page_feedback(request):
    """
    
    """
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            subject = feedback_form.changed_data['subject']
            subject = feedback_form.changed_data['subject']
            email = feedback_form.changed_data['email']
            message = feedback_form.changed_data['message']
            copy = feedback_form.cleaned_data['copy']

            recipient_list = settings.EMAIL_HOST_USER

            if copy:
                recipient_list.append(email)
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            except BadHeaderError:
                return HttpResponse('Обнаружен недопустимый заголовок')
            return HttpResponseRedirect('')
        else:
            pass
    else:
        pass