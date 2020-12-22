from django.urls import path
from django.contrib.sitemaps.views import sitemap

# from django.views.generic.dates import MonthArchiveView


from .sitemaps import PostSitemap
from . import views, feeds

app_name = 'publications'

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('category/<slug:category_slug>/', views.post_list,
         name='post_list_by_category'),
    path('about/', views.display_page_about_blog,
         name='display_page_about_blog'),
    path('contact/', views.display_page_contact, name='display_page_contact'),
    path('search/', views.post_list, name='search'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', feeds.LatestPostsFeed(), name='post_feed'),
    path('archive/<int:year>/<int:month>/',
         views.PostMonthArchiveView.as_view(month_format='%m'),
         name='post_archive_month'),
]
