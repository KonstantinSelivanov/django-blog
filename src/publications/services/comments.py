from typing import Union

from django.contrib.messages.api import debug
from django.db.models import F

from ..forms import CommentForm
from ..models import Comment, Post


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
            Post.published.filter(pk=post.id).update(
                comments=F('comments') + 1)
            comment_form = CommentForm()
        else:
            debug(request, comment_form.errors)
    else:
        comment_form = CommentForm()
    return new_comment, comment_form
