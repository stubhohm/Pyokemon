from ...Keys import npc
from ...Creatures.Wurmple_Line.Full import instance_wurmple, instance_cascoon, instance_silcoon, instance_dustox, instance_beautifly
from ...Function_Lib.Generate_Trainers import generate_bug_trainers
from ...Class_lib.Town import Town
from ...Building_List.BuildingList import make_building
from ...Sprites.MapComponents.Sprites import generate_littleroot_town_map as generate_town_map
from .ValidationArrays import blocked_spaces
from .TallGrassArrays import tall_grass_array
from .TransitionArrays import route_101_entry, route_101_start
from .LedgeArrays import ledge_array

def generate_town():
    town = Town('Littleroot Town')   
    trainers = generate_bug_trainers()
    for trainer in trainers:
        town.add_trainer(trainer)

    map = generate_town_map()
    town.set_sprite(map)
    town.define_blocked_spaced(blocked_spaces)
    transition_dict = {'Route 101' : [route_101_entry, route_101_start]}
    town.define_area_transitions(transition_dict)
    town.define_ledges(ledge_array)
    town.starting_position = (15, 1)
    
    return town
