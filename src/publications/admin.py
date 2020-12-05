from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'status')
    list_filter = ('status', 'created', 'date_published', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_published'
    ordering = ('status', 'date_published')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
