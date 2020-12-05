from django.urls import path

from . import views

app_name = 'publications'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail, name='post_detail'),
]
