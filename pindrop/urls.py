from django.conf.urls import include, url
from rest_framework import routers
from django.contrib import admin
from rapipd import data_factory




urlpatterns = [
    url(r'^', include('rapipd.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^create_data', data_factory.create_data),
    url(r'^delete_data', data_factory.delete_data)
]
