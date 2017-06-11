
from django.conf.urls import url
from django.contrib import admin

from rapipd import views


urlpatterns = [
    url(r'^events', views.allEvents),
    url(r'^groups', views.allGroups),
    url(r'^organizers', views.allOrganizers),
    url(r'^locations', views.allLocations),
    url(r'^categories', views.allCategories),
]
