from django.http import HttpResponse
from .models import Event, Group, Organizer, Location, Category
import secrets


def create_data(self):
    categories_maximum = 21 # -1 times 5 = 100
    locations_maximum = 51 # -1 times 3 = 150
    organizers_maximum = 26 # -1 times 4 = 100
    groups_maximum = 21 # -1 times 3 = 60
    events_maximum = 101 # -1 times 3 = 300

    ## CATEGORIES 
    categories_list = ['Python', 'Django', 'Ruby', 'JavaScript', 'AngularJS']    
    for i in range(1, categories_maximum):
        for category in categories_list:
            name = category+str(i)
            e = Category(category_name=name) 
            e.save()


    ## LOCATIONS
    venue_name_list = ['Tech Valley Center of Gravity', 'Harvard University', 'University of Oxford']  
    address_list = ['30 3rd St, Troy, NY 12180', 'Cambridge, MA 02138', 'Oxford OX1 3BD, UK']
    latitude_list = [42.731191, 42.379399, 51.754870]
    longitude_list = [-73.6906112, -71.115664, -1.254667]
    for i in range(1, locations_maximum):
        for each_venue_name in venue_name_list:
            new_venue_name = each_venue_name+str(i)
            e = Location(
                        venue_name=new_venue_name, 
                        address=secrets.choice(address_list), 
                        latitude=secrets.choice(latitude_list), 
                        longitude=secrets.choice(longitude_list)
                        ) 
            e.save()

    ## ORGANIZERS  
    organizer_first_name_list = ['Misael', 'Ricky', 'Nikita', 'Aaron']
    organizer_last_name_list = ['Virissimo de Moura', 'Meyers', 'Thomas', 'Banewicz']
    for i in range(1, organizers_maximum):
        for each_organizer_first_name in organizer_first_name_list:
            new_organizer_first_name = each_organizer_first_name+str(i)
            new_organizer_email = new_organizer_first_name+"@gmail.com"
            e = Organizer(
                            organizer_email=new_organizer_email, 
                            organizer_first_name=new_organizer_first_name, 
                            organizer_last_name=secrets.choice(organizer_last_name_list), 
                            organizer_cellphone_number= 5180000000
                        ) 
            e.save()


    ## GROUPS
    group_name_list = ['Albany Can Code', 'Google', 'Apple']
    group_description_list = [
        'AlbanyCanCode, was established in the summer of 2016 to serve two key stakeholder groups.',
        'Google is an American multinational technology company specializing in Internet-related services and products. These include online advertising technologies, search, cloud computing, software, and hardware.',
        'Apple Inc. is an American multinational technology company headquartered in Cupertino, California that designs, develops, and sells consumer electronics, computer software, and online services.'
    ] 


    for i in range(1, groups_maximum):
        for each_group_name in group_name_list:
            new_group_name_list = each_group_name+str(i)
            e = Group(
                        group_name=new_group_name_list, 
                        group_description=secrets.choice(group_description_list)
                        ) 
            e.save()
            e.group_categories.add(Category.objects.order_by('?')[:1].get(), Category.objects.order_by('?')[:1].get())
            e.group_organizers.add(Organizer.objects.order_by('?')[:1].get(), Organizer.objects.order_by('?')[:1].get())


    ## EVENTS
    event_name_list = ['DjangoCon Europe', 'ANGULAR SUMMIT', 'Annual SciPy Conference']
    event_date_list = ['2018-04-7', '2018-09-25', '2018-07-10'] 
    event_start_time_list = ['16:00:00', '16:00:00', '16:00:00'] 
    event_end_time_list = ['22:00:00', '22:00:00', '22:00:00'] 
    for i in range(1, events_maximum):
        for each_event_name in event_name_list:
            new_event_name = each_event_name+str(i)
            e = Event(
                        event_name=new_event_name, 
                        event_date=secrets.choice(event_date_list),
                        event_start_time=secrets.choice(event_start_time_list),
                        event_end_time=secrets.choice(event_end_time_list),
                        event_group=Group.objects.order_by('?')[:1].get(),
                        event_location= Location.objects.order_by('?')[:1].get()
                        ) 
            e.save()

    print("You have created:")
    print('categories_maximum', Category.objects.count())
    print('locations_maximum', Location.objects.count())
    print('organizers_maximum', Organizer.objects.count())
    print('groups_maximum', Group.objects.count())
    print('events_maximum', Event.objects.count())

    ## RETURN
    return HttpResponse("<h3>Congrats! You now have a populated database! </h3><br> --> <a href='http://127.0.0.1:8000'> Go check it! </a>")



def delete_data(self):
  print('You have deleted:')
  print('categories_maximum', Category.objects.count())
  print('locations_maximum', Location.objects.count())
  print('organizers_maximum', Organizer.objects.count())
  print('groups_maximum', Group.objects.count())
  print('events_maximum', Event.objects.count())
  e = Category.objects.all().delete()
  e = Location.objects.all().delete()
  e = Organizer.objects.all().delete()
  e = Group.objects.all().delete()
  e = Event.objects.all().delete()

  return HttpResponse('<h3> You have emptied your database. </h3><br> --> <a href="http://127.0.0.1:8000/create_data">Fill up the database</a> <br> --> <a href="http://127.0.0.1:8000">Bak to the  Browsable API</a> ')
