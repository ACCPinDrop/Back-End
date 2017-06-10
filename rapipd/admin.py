from django.contrib import admin
from .models import Group, Event, Organizer, Location, Category
# Register your models here.

admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Organizer)
admin.site.register(Location)
admin.site.register(Category)