
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from rapipd.views import category, location, organizer, group, event

router = routers.DefaultRouter()

router.register(r'categories', category.category_list)
router.register(r'locations', location.location_list)
router.register(r'organizers', organizer.organizer_list)
router.register(r'groups', group.group_list)
router.register(r'events', event.event_list)



urlpatterns = [
    url(r'^', include(router.urls)),
]
