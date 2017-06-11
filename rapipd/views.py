from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Event, Group, Organizer, Location, Category
from django.core import serializers

def allEvents(request):
    events = Event.objects.all()
    events = Event.objects.all().values()  # or simply .values() to get all fields
    events_list = list(events)  # important: convert the QuerySet to a list object
    return JsonResponse(events_list, safe=False)

def allGroups(request):
    groups = Group.objects.all()
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

def newData(request):
    
    ## CATEGORIES
    
    # Python
    e = Category(category_name="Python") 
    e.save()
    # Django
    e = Category(category_name="Django") 
    e.save()
    # Ruby
    e = Category(category_name="Ruby") 
    e.save()
    # JavaScript
    e = Category(category_name="JavaScript") 
    e.save()
    # AngularJS
    e = Category(category_name="AngularJS") 
    e.save()
    
    ## LOCATIONS
    
    # Tech Valley Center of Gravity
    e = Location(venue_name="Tech Valley Center of Gravity", address="30 3rd St, Troy, NY 12180", latitude=42.731191, longitude= -73.6906112) 
    e.save()

    # Harvard University
    e = Location(venue_name="Harvard University", address="Cambridge, MA 02138", latitude=42.379399, longitude= -71.115664) 
    e.save()

    # University of Oxford
    e = Location(venue_name="University of Oxford", address="Oxford OX1 3BD, UK", latitude=51.754870, longitude= -1.254667) 
    e.save()
    
    ## ORGANIZERS
    
    # Misael
    e = Organizer(organizer_email="mvmmisael@gmail.com", organizer_first_name="Misael", organizer_last_name="Virissimo de Moura", organizer_cellphone_number= 5180000000) 
    e.save()

    # Ricky
    e = Organizer(organizer_email="meyers.ricky@gmail.com", organizer_first_name="Ricky", organizer_last_name="Meyers", organizer_cellphone_number= 5180000000) 
    e.save()

    # Nikita
    e = Organizer(organizer_email="f.nikita.thomas@gmail.com", organizer_first_name="Nikita", organizer_last_name="Thomas", organizer_cellphone_number= 5180000000) 
    e.save()

    # Aaron 
    e = Organizer(organizer_email="aaron.banewicz@gmail.com", organizer_first_name="Aaron ", organizer_last_name="Banewicz", organizer_cellphone_number= 5180000000) 
    e.save()
    

    ## GROUPS
    category1 = Category.objects.get(category_name="Ruby").category_name
    category2 = Category.objects.get(category_name="Python").category_name
    category3 = Category.objects.get(category_name="JavaScript").category_name
    category4 = Category.objects.get(category_name="Django").category_name
    category5 = Category.objects.get(category_name="AngularJS").category_name

    organizer1 = Organizer.objects.get(organizer_email="mvmmisael@gmail.com").organizer_email
    organizer2 = Organizer.objects.get(organizer_email="meyers.ricky@gmail.com").organizer_email
    organizer3 = Organizer.objects.get(organizer_email="f.nikita.thomas@gmail.com").organizer_email
    organizer4 = Organizer.objects.get(organizer_email="aaron.banewicz@gmail.com").organizer_email

    # ACC
    e = Group(group_name="Albany Can Code", 
                  group_description="AlbanyCanCode, was established in the summer of 2016 to serve two key stakeholder groups.",
                  ) 
    e.group_categories.add(category1, category2)
    e.group_organizers.add(organizer1, organizer4)
    e.save()

    # Google
    e = Group(group_name="Google", 
                  group_description="Google is an American multinational technology company specializing in Internet-related services and products. These include online advertising technologies, search, cloud computing, software, and hardware.",
                  ) 
    e.group_categories.add(category3, category4)
    e.group_organizers.add(organizer2, organizer3, organizer4)
    e.save()

    # Apple
    e = Group(group_name="Apple", 
                  group_description="Apple Inc. is an American multinational technology company headquartered in Cupertino, California that designs, develops, and sells consumer electronics, computer software, and online services.",
                  ) 
    e.group_categories.add(category2, category4, category3)
    e.group_organizers.add(organizer1, organizer3)
    e.save()

    # EVENTS
    
    group1 = Group.objects.get(group_name="Google")
    group2 = Group.objects.get(group_name="Apple")
    group3 = Group.objects.get(group_name="Albany Can Code")


    location1 = Location.objects.get(venue_name="University of Oxford")
    location2 = Location.objects.get(venue_name="Harvard University")
    location3 = Location.objects.get(venue_name="Tech Valley Center of Gravity")
    
    # DjangoCon Europe
    e = Event(
              event_name="DjangoCon Europe", 
              event_date="2018-04-7",
              event_start_time="16:00:00",
              event_end_time="22:00:00",
              event_group=group1,
              event_location=location1
             )
    e.save()

    # ANGULAR SUMMIT
    e = Event(
              event_name="ANGULAR SUMMIT", 
              event_date="2018-09-25",
              event_start_time="16:00:00",
              event_end_time="22:00:00",
              event_group=group3,
              event_location=location3
             )
    e.save()

    # Annual SciPy Conference
    e = Event(
              event_name="Annual SciPy Conference", 
              event_date="2018-07-10",
              event_start_time="16:00:00",
              event_end_time="22:00:00",
              event_group=group2,
              event_location=location2
             )
    e.save()

    return HttpResponse("Congrats! You now have a populated database! <a href='http://127.0.0.1:8000/all'> Go check it! </a>")

def all(request):
    return HttpResponse('Tables: <br><br><br> - <a href="http://127.0.0.1:8000/all/events">Events</a> <br> - <a href="http://127.0.0.1:8000/all/groups">Groups</a> <br> - <a href="http://127.0.0.1:8000/all/organizers">Organizers</a> <br> - <a href="http://127.0.0.1:8000/all/locations">Locations</a> <br> - <a href="http://127.0.0.1:8000/all/categories">Catgories</a>')
