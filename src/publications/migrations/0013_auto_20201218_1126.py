# Generated by Django 3.1.4 on 2020-12-18 11:26

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0012_auto_20201218_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Содержание поста'),
        ),
    ]
