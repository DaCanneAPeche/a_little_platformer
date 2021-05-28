import json

def get_all_maps():

    with open('assets/maps/maps.json') as maps:

        all_maps = json.load(maps)

    return all_maps
