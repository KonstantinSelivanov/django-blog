# Generated by Django 3.1.4 on 2020-12-07 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=80, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('body', models.TextField(verbose_name='Коментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания комментария')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения комментария')),
                ('moderation', models.BooleanField(default=True, verbose_name='Модерация')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications_comments', to='publications.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'db_table': 'comments',
                'ordering': ('created',),
            },
        ),
    ]
