from django.urls import path

from . import views
# from . import templatetags
# from publications.templatetags import tags_services
# from publications.templatetags import tags_services
app_name = 'publications'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('tag/<slug:category_slug>/', views.post_list, name='post_category1')
    # path('detail/<slug:slug>/', tags_services.show_all_categories, name='post_category')
]
