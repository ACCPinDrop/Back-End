from django.contrib import admin
from .models import Group, Event, Organizer, Location, Category
# Register your models here.


class readOnly(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', )


admin.site.register(Group, readOnly)
admin.site.register(Event, readOnly)
admin.site.register(Organizer, readOnly)
admin.site.register(Location, readOnly)
admin.site.register(Category, readOnly)