from django.urls import path

from . import views

app_name = 'publications'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('category/<slug:category_slug>/',
         views.post_list, name='post_list_by_category'),
    path('about/',
         views.display_page_about_blog, name='display_page_about_blog'),
    path('contact/', views.display_page_contact, name='display_page_contact'),
    path('search/', views.search, name='search'),
]
