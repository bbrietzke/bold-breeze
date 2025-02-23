from django.core.management.base import BaseCommand, CommandError
from builder.models import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


class Command(BaseCommand):
    help = "Syncs between master unit list and the local database"

    def handle(self, *args, **options):
        # page = urlopen("http://masterunitlist.info/Unit/Filter?Name=&HasBV=true&Rules=6").read().decode("utf-8") # experimental
        # page = urlopen("http://masterunitlist.info/Unit/Filter?Name=&HasBV=true&Rules=5").read().decode("utf-8") # Advanced
        # page = urlopen("http://masterunitlist.info/Unit/Filter?Name=&HasBV=true&Rules=4").read().decode("utf-8") # Standard
        # page = urlopen("http://masterunitlist.info/Unit/Filter?Name=&HasBV=true&Rules=55").read().decode("utf-8") # Introductory
        page = urlopen("http://masterunitlist.info/Unit/Filter?Name=&HasBV=true&Rules=5&Rules=4&Rules=55").read().decode("utf-8") # Standard and Introductory
        soup = BeautifulSoup(page, 'html.parser')
        all_rows = soup.find_all('tr')

        for row in all_rows:
            a_tag = row.find('a', href=True)
            if a_tag is None:
                continue
            searched = re.search(r'\d+', a_tag['href'])
            if searched is None:
                continue
            name = a_tag.string
            master_unit_list_number = searched.group()
            items = list(row.children)
            if items[5].string is None:
                continue
            tonnage = round(float(items[5].string.replace(',', '')))
            battle_value = items[7].string.replace(',', '')
            point_value = items[9].string
            unit_role_text = items[11].string
            rules_level_text = items[15].string
            date_introduced = items[19].string
            #print(name, master_unit_list_number, battle_value, date_introduced)
            if point_value is None:
                continue
            if not isinstance(date_introduced, int):
                if 'Unknown' in date_introduced:
                    date_introduced = 1950
                elif 'PS' in date_introduced:
                    date_introduced = 1960
                elif 'ES' in date_introduced:
                    date_introduced = 1965
                elif 'circa' in date_introduced:
                    date_introduced = 2300
            if Unit.objects.filter(master_unit_list_number = master_unit_list_number).count() == 0:
                if RulesLevel.objects.filter(level=rules_level_text).count() == 0:
                    l = RulesLevel(level = rules_level_text)
                    l.save()
                if UnitRole.objects.filter(role=unit_role_text).count() == 0:
                    l = UnitRole(role = unit_role_text)
                    l.save()
                rules_level = RulesLevel.objects.get(level = rules_level_text) 
                unit_role = UnitRole.objects.get(role = unit_role_text) 
                unit = Unit(master_unit_list_number = master_unit_list_number, name = name, unit_role = unit_role, tonnage = tonnage, battle_value = battle_value, point_value = point_value, rules_level = rules_level, date_introduced = date_introduced)
                unit.save()
            else:
                pass