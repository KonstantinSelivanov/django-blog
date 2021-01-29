from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('', include('pages.urls', namespace='pages')),
    path('', include('feedback.urls', namespace='feedback')),
    path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
