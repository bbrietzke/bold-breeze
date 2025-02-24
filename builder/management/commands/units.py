from django.core.management.base import BaseCommand, CommandError
from math import ceil
from builder.models import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class Command(BaseCommand):
    help = "Syncs between master unit list and the local database"

    def handle(self, *args, **options):
        units = Unit.objects.order_by('master_unit_list_number')

        for unit in units:
            url = "http://masterunitlist.info/Unit/Details/{0}/".format(unit.master_unit_list_number)
            print(url)
            page = urlopen(url).read().decode("utf-8")
            soup = BeautifulSoup(page, 'html.parser')
            list = soup.find_all('dd')

            era_text = list[8].string
            technology_text = list[4].string
            unit_type_text = list[5].string
            cost = list[2].string.replace(',','')

            if Technology.objects.filter(name = technology_text).count() == 0:
                t = Technology(name = technology_text)
                t.save()

            if UnitType.objects.filter(type = unit_type_text).count() == 0:
                t = UnitType(type = unit_type_text)
                t.save()

            if Era.objects.filter(era = era_text).count() == 0:
                t = Era(era = era_text)
                t.save()

            if 'NA' in cost:
                cost = 0
            
            unit.cost = cost
            unit.era = Era.objects.get(era = era_text)
            unit.technology = Technology.objects.get(name = technology_text)
            unit.unit_type = UnitType.objects.get(type = unit_type_text)

            unit.save()