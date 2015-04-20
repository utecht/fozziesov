import sqlite3
from lxml import etree


conn = sqlite3.connect("../../universeDataDx.db")
cur = conn.cursor()
cur.execute("""
    select solarSystemID
    from mapSolarSystems
    join mapRegions
        on mapSolarSystems.regionID = mapRegions.regionID
    join mapConstellations
        on mapConstellations.regionID = mapSolarSystems.regionID
        and mapConstellations.constellationID = mapSolarSystems.constellationID
    where regionName = "Wicked Creek"
      and constellationName = "J-9M7D"

    order by solarSystemName
""")

ids = [str(i) for i, in cur]
conn.close()


def matches(name):
    for id in ids:
        if id in name:
            return True
    return False

filename = "test3.svg"
tree = etree.parse(open(filename, 'r'))

to_delete = []
for element in tree.iter():
    # all symbols, test that they contain an id
    # all lines, test that they contain an id
    el_name = element.tag.split("}")[1]
    
    if el_name in ['g', 'standings', 'notes', 'highlights']:
        id = element.get("id")
        if id == 'legend':
            to_delete.append(element)

    if el_name in ['symbol', 'line']:
        id = element.get("id")
        if matches(id):
            print(id)
        else:
            to_delete.append(element)


for el in to_delete:
    el.getparent().remove(el)

f = open('out.svg', 'wb')
t = etree.tostring(tree, pretty_print=True)
f.write(t)
f.close()
