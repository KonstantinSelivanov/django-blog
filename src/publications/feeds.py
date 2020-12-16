from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from config import settings

from .models import Post, PublishedManager


class LatestPostsFeed(Feed):
    """
    Automatic RSS generation.
    Автоматическая генерация RSS.
    """
    title = settings.SITE_NAME
    link = ''
    description = 'Новые посты'

    def items(self, count=5) -> PublishedManager:
        """
        Get objects that will be included in the mailing list.
        By default, the 5 most recent blog posts.
        Получить объекты которые будут включены в рассылку.
        По умолчанию 5 последних постов блога.
        """
        return Post.published.all()[:count]

    def item_title(self, item: str) -> str:
        """
        Get the title in the form of the name of the blog site.
        Получить заголовок вв виде названия сайта-блога.
        """
        return item.title

    def item_description(self, item: str) -> str:
        """
        Get a feed description. Limit post descriptions to thirty words.
        Получить описание фида. Ограничить описание постов тридцатью словами.
        """
        return truncatewords(item.body, 70)
