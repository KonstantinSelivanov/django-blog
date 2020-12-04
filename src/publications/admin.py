from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'status_post')
    list_filter = ('status_post', 'created', 'date_published', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_published'
    ordering = ('status_post', 'date_published')
