from rapipd.models import Event, Group, Organizer, Location, Category

e = Event(event_name="First Event", event_date="2017-08-11", event_start_time="13:58:46", event_end_time="18:58:46", event_group="ACC", event_location="My House") 
e.save()