from django.contrib import admin

from .models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date_published', 'status', 'hits', 'comments')
    list_filter = ('status', 'created', 'date_published', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_published'
    ordering = ('status', 'date_published')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'post', 'created', 'moderation')
    list_filter = ('moderation', 'created', 'updated')
    search_fields = ('author', 'email', 'body')


# @admin.register(Visitor)
# class VisitorAdmin(admin.ModelAdmin):
#     list_display = ('created', 'ip', 'session', 'user_agent')
