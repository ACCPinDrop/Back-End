from django.shortcuts import render
from django.http import JsonResponse
from .models import Event, Group, Organizer, Location, Category

def allEvents(request):
    events = Event.objects.all()
    events = Event.objects.all().values()  # or simply .values() to get all fields
    events_list = list(events)  # important: convert the QuerySet to a list object
    return JsonResponse(events_list, safe=False)

def allGroups(request):
    goups = Group.objects.all()
    goups = Group.objects.all().values() 
    goups_list = list(goups) 
    return JsonResponse(goups_list, safe=False)

def allOrganizers(request):
    organizers = Organizer.objects.all()
    organizers = Organizer.objects.all().values()
    organizers_list = list(organizers)
    return JsonResponse(organizers_list, safe=False)

def allLocations(request):
    locations = Location.objects.all()
    locations = Location.objects.all().values() 
    locations_list = list(locations)  
    return JsonResponse(locations_list, safe=False)

def allCategories(request):
    categories = Category.objects.all()
    categories = Category.objects.all().values() 
    categories_list = list(categories) 
    return JsonResponse(categories_list, safe=False)