
from django.contrib import admin
from django.urls import path,re_path

from blog import views as blog_views
from blog import views
from django.conf.urls import url

#drf模块************************************************************
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from dj_rest_auth.registration.views import VerifyEmailView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index),
    # path('', blog_views.python_file),






]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 使用nigx部署的时候就不需要这么设置了，转发静态文件就可以了，只是调试的需要这么操作
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
