from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify as slugify_ru
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class PublishedManager(models.Manager):
    """
    Own model manager.
    Собственный менеджер модели.
    """
    def get_queryset(self):
        """
        Returns a QuerySet filtered by status = 'published'. A QuerySet with
        posted posts will be returned.
        Возвращает QuerySet с фильтром по status='published'. Будет возвращен
        QuerySet с опубликованными постами.
        """
        return super(PublishedManager, self) \
            .get_queryset() \
            .filter(status='published')


class Post(models.Model):
    """
    Data model for blog posts.
    Модель данных для публикаций блога.
    """
    STATUS_CHOICES = (
        ('draft', 'черновик'),
        ('published', 'опубликовано')
    )

    title = models.CharField(verbose_name='Заголовок поста', max_length=250)
    slug = models.SlugField(verbose_name='URL',
                            max_length=250,
                            blank=True,
                            unique_for_date='date_published')
    author = models.ForeignKey(User,
                               verbose_name='Автор поста',
                               on_delete=models.CASCADE,
                               related_name='publications_posts')
    body = models.TextField(verbose_name='Содержание поста')
    date_published = models.DateTimeField(verbose_name='Дата публикации поста',
                                          default=timezone.now)
    created = models.DateTimeField(verbose_name='Дата написания поста',
                                   auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата обновления поста',
                                   auto_now=True)
    status = models.CharField(verbose_name='Статус',
                              max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-date_published',)
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        db_table = 'posts'

    def __str__(self):
        return self.title

    def slugify(self, s):
        """
        Overriding the standard slugify () function, which also allows
        the use of Russian words in slug.
        Переопределение стандартной функции slugify(), позволяющей также
        использовать русские слова в slug.
        """
        ALPHABET_RU = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g',
                       'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
                       'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k',
                       'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
                       'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
                       'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
                       'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i',
                       'э': 'e', 'ю': 'yu', 'я': 'ya'}
        return slugify_ru(''.join(ALPHABET_RU.get(w, w) for w in s.lower()))

    def save(self, *args, **kwargs):
        """
        Overridden standard save() function. Serves for automatic slug
        creation. If the post has no slug, the slugify() function
        automatically forms it from the passed header, after which
        the post object is saved.
        Переопределенная стандартная функция save(). Служит для автоматического
        формирования slug. Если у поста нет слага, функция slugify()
        автоматически формирует его из переданного заголовка, после чего
        происходит сохранение объекта поста.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        The function generates direct links.
        Функция формирует прямые ссылки.
        """
        return reverse('publications:post_detail', args=[self.id, self.slug])
