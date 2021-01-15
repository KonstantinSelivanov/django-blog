from django.urls import path

from . import views

app_name = 'pages'


urlpatterns = [
    path('about/', views.display_page_about_blog,
         name='display_page_about_blog'),
    path('contact/', views.display_page_contact, name='display_page_contact'),
]
