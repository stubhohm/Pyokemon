from ...Keys import npc
from ...Creatures.Wurmple_Line.Full import instance_wurmple, instance_cascoon, instance_silcoon, instance_dustox, instance_beautifly
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Building import Building
from ...Class_lib.Route import Route
from ...Sprites.MapComponents.Sprites import generate_route_101_map as generate_route_map
from .ValidationDict import blocked_spaces_dict
from .TallGrassDict import tall_grass_dict
from .LedgeDict import ledge_dict, ledge_tops_dict
from .WaterDict import water_dict
from .TransitionArrays import north_entry, north_start, east_entry, east_start
from .TransitionArrays import west_entry, west_start, south_entry, south_start

route_name = 'Name'
north_area_name = 'N'
east_area_name = 'E'
west_area_name = 'W'
south_area_name = 'S'

# Primary called function by other documents
def generate_route():
    route = Route(route_name)   
    set_map(route)
    set_dicts(route)
    set_grass(route)
    set_transitions(route)
    set_trainers(route)

    return route

def set_grass(route:Route):
    grass = TallGrass('Grass')
    grass.add_pokemon(instance_cascoon, [10,12], 5)
    grass.add_coordinates(tall_grass_dict)
    route.add_tall_grass(grass)

def set_trainers(route:Route):
    trainers = generate_bug_trainers()
    for trainer in trainers:
        route.add_trainer(trainer)

def set_buildings(route:Route):
    buildings = []
    for building in buildings:
        if type(building) != Building:
            continue
        route.add_building(building)


# Below functions occur with no input after dictionaries and arrays are made in the other files

def set_transitions(route:Route):
    transition_dict = {}
    transition_dict[north_area_name] = [north_entry, north_start]
    transition_dict[east_area_name] = [east_entry, east_start]
    transition_dict[south_area_name] = [south_entry, south_start]
    transition_dict[west_area_name] = [west_entry, west_start]
    route.define_area_transitions(transition_dict)

def set_dicts(route:Route):
    route.define_ledges(ledge_dict)
    route.define_ledge_tops(ledge_tops_dict)
    route.define_blocked_spaced(blocked_spaces_dict)
    route.define_water(water_dict)

def set_map(route:Route):
    map = generate_route_map()
    route.set_sprite(map)
