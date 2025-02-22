from django.core.management.base import BaseCommand, CommandError
from builder.models import *


class Command(BaseCommand):
    help = "Syncs between master unit list and the local database"

    def handle(self, *args, **options):
        pass