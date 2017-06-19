
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from rapipd.views import category, location, organizer, group, event

router = routers.DefaultRouter()

router.register(r'categorys', category.category_list)
router.register(r'locations', location.location_list)
router.register(r'organizers', organizer.organizer_list)
router.register(r'groups', group.group_list)
router.register(r'events', event.event_list)



urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^categories/$', category.category_list),
    # url(r'^categories/(?P<pk>[0-9]+)/$', category.category_detail),
    # url(r'^locations/$', location.location_list),
    # url(r'^locations/(?P<pk>[0-9]+)/$', location.location_detail),
    # url(r'^organizers/$', organizer.organizer_list),
    # url(r'^organizers/(?P<pk>[0-9]+)/$', organizer.organizer_detail),
    # url(r'^groups/$', group.group_list),
    # url(r'^groups/(?P<pk>[0-9]+)/$', group.group_detail),
]
