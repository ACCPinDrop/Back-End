from django.db import models

# Create your models here.

class TimeStamp(models.Model):
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()

	# Tells django and migration system that this model isn't
	# to be used to store data, but once inherited things will work.
	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		# If object is not already created, created_at and updated_at will be set
		if not self.id:
			self.created_at = timezone.now()
		self.updated_at = timezone.now() # Otherwise updated at will be set
		return super(User, self).save(*args, **kwargs)

class Location(TimeStamp):
	address = models.CharField(max_length=50)
	venue_name = models.CharField(max_length=50)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)

	def __str__(self):
		return self.venue_name

class Organizer(TimeStamp):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	cellphone_number = models.CharField(max_length=10)

	def __str__(self):
		return u'%s %s' %(self.first_name, self.last_name)

class Category(models.Model):
	category_name = models.CharField(max_length=25)

	def __str__(self):
		return self.category_name

class Group(TimeStamp):
	group_name = models.CharField(max_length=50)
	description = models.TextField()
	group_url = models.URLField(blank=True)
	picture = models.ImageField(blank=True)
	category = models.ManyToManyField(Category, blank=True)
	organizer = models.ForeignKey(Organizer)

	def __str__(self):
		return self.group_name

class Meeting(TimeStamp):
	meeting_name = models.CharField(max_length=50)
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	location = models.ForeignKey(Location)

	def __str__(self):
		return self.meeting_name
