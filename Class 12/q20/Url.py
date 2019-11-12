from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='homepage'),
    url(r'^page1/$', views.page1, name='authpage')
]
