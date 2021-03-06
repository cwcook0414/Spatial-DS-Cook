"""
Program:
--------
    Program 4 - Generating geo json from json files

Description:
------------
    This program reads in a particular json file and converts it to a geo json format.
    
Name: Chris W Cook
Date: 28 June 2017
"""
import pprint as pp
import os,sys
import json
import collections

dir_path = os.path.dirname(os.path.realpath(__file__))

f = open(dir_path+"\\WorldData\\earthquakes-1960-2017.json","r")

data = f.read()

data = json.loads(data)

all_earthquakes = []

for key,value in data.items():
        for c in value:
            gj = collections.OrderedDict()

            gj['type'] = 'Feature'
            gj['properties'] = c
            lat = c['geometry']['coordinates'][1]
            lon = c['geometry']['coordinates'][0]
            del gj['properties']['geometry']
            gj['geometry'] = {}
            gj['geometry']['type'] = 'Point'
            gj['geometry']['coordinates'] = [lon,lat]
            all_earthquakes.append(gj)
            


out = open(dir_path+"\\geo_json\\earthquakes_gj.geojson","w")

out.write(json.dumps(all_earthquakes, sort_keys=False,indent = 4, separators = (',',':')))

out.close()