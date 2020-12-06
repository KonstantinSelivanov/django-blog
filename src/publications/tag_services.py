from django import template

from .models import Post


# A module-level variable named register, which is an instance
# of template.Library in which all tags and filters are registered.
# Переменна уровня модуля с именем register, которая является экземпляром
# template.Library, в котором зарегистрированы все теги и фильтры.
register = template.Library()

# Decorator for registering a new tag
# Декоратор для регистрации нового тега
@register.tag(name='total_posts')
def total_posts():
    # Returns the number of posts published
    # Возвращает количество опубликованных постов
    return Post.published.count()
