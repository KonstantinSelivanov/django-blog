from django.contrib import admin

from .models import About, Contact


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
