from django.core.management.base import BaseCommand
from builder.utils import beautify_the_soup
from builder.models import *
import re

class Command(BaseCommand): 
    help = "Blah, blah, blah"

    def handle(self, *args, **options):
        all_eras = beautify_the_soup("http://masterunitlist.info/Era/Index") \
            .find_all('div', {"class": "col-xs-4 pad-after"})

        for era in all_eras:
            name = era.select_one('h3').string.strip()
            link = re.search(r"/Era/Details/(?P<era>\d+)/(?P<slug>\w+(?:-*?\w+)+)", era['data-link'])
            master_unit_list_id = link.group('era')
            slug = link.group('slug')    
            dates = re.search(r"\((?P<start>\d+)-(?P<end>\d+)\)", era.select_one('div').string)
            start = dates.group('start')
            end = dates.group('end')
            new_era = Era(name = name, master_unit_list_id = master_unit_list_id, slug = slug, start = start, end = end)
            new_era.save()



