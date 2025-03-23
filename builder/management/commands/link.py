from django.core.management.base import BaseCommand
from builder.utils import beautify_the_soup
from builder.models import *
import re
import urllib
import urllib.error

class Command(BaseCommand): 
    help = "Blah, blah, blah"

    def handle(self, *args, **options):
        pass
    
for faction in Faction.objects.all():
    for era in all_eras:
        url = "http://masterunitlist.info/Era/FactionEraDetails?FactionId={0}&EraId={1}" \
            .format(faction.master_unit_list_id, era.master_unit_list_id)
        try:
            results = beautify_the_soup(url).find_all('tr')
            if results is None:
                continue
            else:
                faction.eras.add(era)
                faction.save()
                master_unit_list_id = results.find('a')
                print(master_unit_list_id)
        except urllib.error.HTTPError as e:
            if e.code == 500:
                continue
            else:
                raise e





                