import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")
import django
django.setup()

from main.models import *
import sqlite3
import sys

if len(sys.argv) == 1:
    print("Please pass the sqlite static database file")
    exit()

conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()
c.execute("""
        select mapConstellations.constellationID, constellationName, regionName, solarsystemID, solarsystemName from mapSolarSystems
        join mapConstellations on mapConstellations.constellationID = mapSolarSystems.constellationID
        join mapRegions on mapRegions.regionID = mapConstellations.regionID
        """)
for row in c:
    print(row)
    const_id, const_name, region_name, system_id, system_name = row
    const, created = Constellation.objects.get_or_create(const_id=const_id)
    if created:
        const.name = const_name
        const.region = region_name
        const.save()
    system, created = System.objects.get_or_create(system_id=system_id, constellation=const)
    if created:
        system.name = system_name
        system.save()

