from django.core.management.base import BaseCommand
from builder.utils import beautify_the_soup
from builder.models import *
import re

class Command(BaseCommand): 
    help = "Blah, blah, blah"

    def handle(self, *args, **options):
        all_factions = beautify_the_soup("http://masterunitlist.info/Faction/Index") \
            .find_all('div', {"class": "pad-after pad-before filterable"})

        for faction in all_factions:
            name = faction.select_one('strong').string
            link = re.search(r"/Faction/Details/(?P<faction>\d+)", faction['data-link'])
            master_unit_list_id = link.group('faction')
            new_faction = Faction(name = name, master_unit_list_id = master_unit_list_id)
            new_faction.save()



