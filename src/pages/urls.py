from django.urls import path

from . import views

app_name = 'pages'


urlpatterns = [
    path('about/', views.display_page_about,
         name='display_page_about'),
]
