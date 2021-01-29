from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSitemap(Sitemap):
    """
    Sitemap.
    Карта сайта.
    """
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        """
        Return QuerySet objects to be displayed in the sitemap.
        Возвратить QuerySet объекты которые будут отображаться в карте сайта.
        """
        return Post.published.all()

    def lastmod(self, obj):
        """
        The lastmod () method takes each object from the result of the items()
        call and returns the time the post was last modified.
        Метод lastmod() принимает каждый объект из результата вызова items()
        и возвращает время последней модификации статьи
        """
        return obj.updated
