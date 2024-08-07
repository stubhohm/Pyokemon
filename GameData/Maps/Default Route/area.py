from ...Keys import npc
from ...Creatures.Wurmple_Line.Full import instance_wurmple, instance_cascoon, instance_silcoon, instance_dustox, instance_beautifly
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.TallGrass import TallGrass
from ...Class_lib.Route import Route
from ...Sprites.MapComponents.Sprites import generate_route_101_map as generate_route_map
from .ValidationArrays import blocked_spaces
from .TallGrassArrays import tall_grass_array
from .LedgeArrays import ledge_array
from .TransitionArrays import west_entry, west_town_start
from .TransitionArrays import oldale_entry, oldale_start_position


def make_grass():
    easy_grass = TallGrass('Easy Grass')
    easy_grass.add_pokemon(instance_cascoon, [10,12], [0,30])
    easy_grass.add_pokemon(instance_silcoon, [10,12], [31,60])
    easy_grass.add_pokemon(instance_wurmple, [3,7], [61,100])
    easy_grass.add_coordinates(tall_grass_array)
    return easy_grass


def generate_route():
    route = Route('Route 102')   
    
    tall_grass = make_grass()
    
    route.add_tall_grass(tall_grass)
    trainers = generate_bug_trainers()
    for trainer in trainers:
        route.add_trainer(trainer)

    map = generate_route_map()
    route.set_sprite(map)
    route.define_blocked_spaced(blocked_spaces)
    route.define_ledges(ledge_array)
    transition_dict = {'Littleroot Town' : [west_entry, west_town_start]}
    transition_dict['Oldale Town'] = [oldale_entry, oldale_start_position]
    route.define_area_transitions(transition_dict)
    return route
