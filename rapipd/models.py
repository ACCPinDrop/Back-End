from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.

class Location(models.Model):
    address = models.CharField(max_length=200)
    venue_name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.venue_name)

class Organizer(models.Model):
    organizer_email = models.EmailField(max_length=254, primary_key=True, unique=True)
    organizer_first_name = models.CharField(max_length=20, blank=True)
    organizer_last_name = models.CharField(max_length=50, blank=True) 
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    organizer_cellphone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.organizer_first_name)

class Category(models.Model):
    category_name = models.CharField(max_length=50, primary_key=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.category_name)

class Group(models.Model):
    group_name = models.CharField(max_length=50, primary_key=True, unique=True)
    group_description = models.TextField()
    # file will be saved to MEDIA_ROOT/uploads/2017-01-30
    group_picture = models.ImageField(upload_to='images/%Y-%m-%d/')
    group_categories = models.ManyToManyField(Category)
    group_organizers = models.ManyToManyField(Organizer)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.group_name)

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_date = models.DateField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    event_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    event_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%s' % (self.event_name)