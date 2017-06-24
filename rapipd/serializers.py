from rest_framework import serializers
from rapipd.models import Category, Location, Organizer, Group, Event

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ('url', 'id', 'category_name', 'created_at', 'updated_at')

class LocationsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Location
		fields = ('url', 'id', 'venue_name', 'address', 'latitude', 'longitude')

class OrganizerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Organizer
		fields = ('url', 'id', 'organizer_email', 'organizer_first_name', 'organizer_last_name', 'organizer_cellphone_number')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Group
	    fields = ('url', 'id', 'group_name', 'group_description', 'group_picture', 'group_categories', 'group_organizers')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Event
	    fields = ('url', 'id', 'event_name', 'event_date', 'event_start_time', 'event_end_time', 'event_group', 'event_location')