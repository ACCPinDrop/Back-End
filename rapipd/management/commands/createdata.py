from django.core.management.base import BaseCommand, CommandError
# from rapipd.models import Category
from rapipd.views import create_data

class Command(BaseCommand):
    help = 'Creates a sample data and save into the tables'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
            return create_data(self)