#!/usr/bin/env python3

import sqlite3
from lxml import etree


conn = sqlite3.connect("../universeDataDx.db")
cur = conn.cursor()


def handle_one_region(region):
    # get the list of constellations in this region
    cur.execute("""

        select distinct constellationName
        from mapSolarSystems
        join mapRegions
            on mapSolarSystems.regionID = mapRegions.regionID
        join mapConstellations
            on mapConstellations.regionID = mapSolarSystems.regionID
            and mapConstellations.constellationID = mapSolarSystems.constellationID
        where regionName = :region
    """, {'region': region})

    constellations = [i for i, in cur]

    for c in constellations:
        handle_one_const(region, c)

def to_filename(region):
    region = region.replace(' ', '_')
    return region

def handle_one_const(region, const):
    cur.execute("""
        select solarSystemID
        from mapSolarSystems
        join mapRegions
            on mapSolarSystems.regionID = mapRegions.regionID
        join mapConstellations
            on mapConstellations.regionID = mapSolarSystems.regionID
            and mapConstellations.constellationID = mapSolarSystems.constellationID
        where regionName = :region
            and constellationName = :const

        order by solarSystemName
                """, {'region': region, 'const': const})

    ids = [str(i) for i, in cur]


    def matches(name):
        for id in ids:
            if id in name:
                return True
        return False

    filename = "dotlan/{}.svg".format(to_filename(region))
    tree = etree.parse(open(filename, 'r'))

    to_delete = []
    for element in tree.iter():
        # all symbols, test that they contain an id
        # all lines, test that they contain an id
        el_name = element.tag.split("}")[1]
        id = element.get("id")

        # delete these elements entirely
        if el_name in ['script']:
            to_delete.append(element)

        # delete groups based on element ID
        if el_name == 'g':
            if id in ['legend', 'standings', 'notes', 'highlights', 'controls', 'glow']:
                to_delete.append(element)

        # delete unless they match the current system id
        if el_name in ['symbol', 'line', 'use']:
            if matches(id):
                # print(id)
                pass
            else:
                to_delete.append(element)

        # remove the label text, but keep the labels
        # also remove the debug text
        if el_name == 'text':
            if id and id.startswith('txt'):
                element.text = ""
            if id == 'debug':
                to_delete.append(element)

        # adjust the style
        if el_name == 'rect':
            if id and id.startswith('rect'):
                element.set('style', 'fill: #EFEAE0;')
            if id and id.startswith('ice'):
                to_delete.append(element)


        # attempt to delete the station services box
        if el_name in ['rect', 'polygon']:
            class_ = element.get('class')
            if class_ and (class_.startswith('o')
                           or class_.startswith('v')):
                to_delete.append(element)


    for el in to_delete:
        el.getparent().remove(el)

    f = open('const/{}.svg'.format(const), 'wb')
    t = etree.tostring(tree, pretty_print=True)
    f.write(t)
    f.close()
    print(const)


cur.execute("""
    select distinct regionName
    from mapRegions
""")

regions = [r for r, in cur]
for r in regions:
    try:
        handle_one_region(r)
    except FileNotFoundError:
        print("Looks like we don't have a map for region: {}".format(r))

conn.close()
