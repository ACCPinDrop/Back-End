from django.test import TestCase
from rapipd.models import Location

# Create your tests here.
class LocationTestCase(TestCase):
	def LocationTest(self):
		Location.objects.create(address="37 Grand View", venue_name=255, latitude=132.2135, longitude=324.2163)

