"""ubwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from gallery import views
admin.site.site_header = "Utkrishta Bharath Admin"
admin.site.site_title = "Utkrishta Bharath Admin Panel"
admin.site.index_title = "Welcome to Utkrishta Bharath Admin Panel"
from django.contrib.auth.decorators import user_passes_test

urlpatterns = [
            # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
            path('ub_admin/', admin.site.urls),
            # path('tinymce/',include('tinymce.urls')),
            path('', include('blog.urls')),
            path('', include('regi.urls')),
            path('', include('non_blogs.urls')),
            # path('', include('community.urls')),
            path('', include('forum.urls')),
            path('', include('indic_r.urls')),
            path('', include('no_login_forum.urls')),
            
            path('gallery/',views.home, name="home"),
            path('<int:image_id>',views.details, name="details"),
            path('image_like/<int:id>',views.addlike, name="image_like"),
            # path('gallery_image/upload',views.image_upload, name="image-upload")
            path('gallery_image/upload', user_passes_test(views.is_admin)(views.image_upload), name="image-upload"),
            # path("", include("allauth.urls")),
            # re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
] 
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG is True:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)