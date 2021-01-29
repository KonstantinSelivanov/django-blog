from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class About(models.Model):
    """
    Model about blog.
    Модель страница о блоге.
    """
    title = models.CharField(verbose_name='Заголовок страницы', max_length=250)
    body = RichTextUploadingField(verbose_name='Содержание страницы')
    created = models.DateTimeField(verbose_name='Дата написания',
                                   auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата обновления',
                                   auto_now=True)

    class Meta:
        verbose_name = 'страницу о блоге'
        verbose_name_plural = 'Cтраница о блоге'
        db_table = 'about'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise ValueError('Может быть только одна страница о блоге')
        return super(About, self).save(*args, **kwargs)
