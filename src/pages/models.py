from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


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
        verbose_name = 'Cтраницу о блоге'
        verbose_name_plural = 'Cтраница о блоге'
        db_table = 'about'

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    Contact page model.
    Модель страницы контактов.
    """
    title = models.CharField(verbose_name='Заголовок страницы', max_length=250)
    body = RichTextUploadingField(verbose_name='Содержание страницы')
    created = models.DateTimeField(verbose_name='Дата написания',
                                   auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата обновления',
                                   auto_now=True)

    class Meta:
        verbose_name = 'Cтраницу контактов'
        verbose_name_plural = 'Cтраница контактов'
        db_table = 'contact'

    def __str__(self):
        return self.title
