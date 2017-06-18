from django.conf.urls import include, url
from rest_framework import routers
from django.contrib import admin
from rapipd import views_old




urlpatterns = [
    url(r'^', include('rapipd.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^create_data', views_old.create_data),
    url(r'^delete_data', views_old.delete_data)
]
